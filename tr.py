import pandas as pd
import streamlit as st

st.title('Il modello più semplicistico di analisi dei costi del nucleare')
st.header('Nuclear is :blue[cool] :sunglasses:', divider='rainbow')
st.write("Questa app è stata creata da [Umberto Bertonelli](https://umbertobertonelli.it).")
st.write("La documentazione completa è disponibile [qui](https://github.com/DrElegantia/femminicidi_italia/tree/main).")
st.divider()

st.write("L'applicativo in questione è uno strumento che permette agli utenti di stimare i costi e il tempo di realizzazione di un progetto di energia nucleare. Il modello è basato su alcuni parametri, come il tasso di interesse, il tempo di realizzazione, il costo base annuale del progetto, il tasso di apprendimento e il numero di reattori da basare il modello. Il programma permette di scegliere l'anno di partenza del progetto e i tassi di crescita e deficit economici del paese senza nucleare. Il modello fornisce risultati in forma di grafici, tra cui uno che mostra il costo complessivo del progetto in relazione al numero di progetti realizzati, e un altro che mostra l'andamento del costo nel tempo. Il modello ha delle limitazioni, come la mancanza di considerazione di fattori come la variabilità dei costi di capitale e operativi, la capacità di gestire il rischio e la sicurezza, e la capacità di integrare il nucleare con altre fonti di energia rinnovabili. Tuttavia, il modello è utile per fornire una stima grossolana iniziale dei costi e del tempo di realizzazione di un progetto di energia nucleare.")

st.write("Se si vuole approfondire il tema attraverso documenti e opinione di esperti, qui trovate un'intervista al prof. Jacopo Buongiorno, Direttore del Centro per i sistemi avanzati di energia nucleare al MIT")
# URL del video su YouTube
video_url = "https://youtu.be/FOqnCk1Uv7I"

# Incorpora il video nella tua app Streamlit
st.video(video_url)

st.divider()

i = st.slider(
    'Che tasso di  interesse prevedi per il costo del progetto?',
    4, 20,4)
t = st.slider(
    'In quanto tempo stimi venga realizzato il FOAK?',
    4, 30,7)

Progetti = st.slider(
    'Su quanti reattori vuoi basare il modello?',
    1, 30,26)
partenza = st.slider(
    'In che anno parte il progetto?',
    2028, 2050,2029)
apprendimento = st.slider(
    'Che tasso di apprendimento stimi? Il tasso avrà effetto sia sul tempo di realizzazione che sul costo',
    1, 10,3)
Costo_base=st.slider(
    'Quanto stimi possa costare il FOAK annualmente? Seleziona un dato in miliardi di €',
    1.0, 5.0,1.0)
pil=st.slider(
    f'A quanto stimi il pil nominale italiano al {partenza}? In miliardi di €',
    1800, 3000,1900)
debito=st.slider(
    f'A quanto stimi il debito nominale italiano al {partenza}? In miliardi di €',
    2700, 3000,2900)

crescita=st.slider(
    f'A che tasso ritieni possibile che cresca mediamente il paese senza nucleare? Il fondo monetario stima una crescita pari a 1%',
    0, 15,1)
deficit=st.slider(
    f'Quanto deficit credi faccia mediamente il paese senza nucleare? Il fondo monetario stima un deficit pari a 3%',
    0, 15,3)



def costo_opera(i, t, co):
  costo_opera=co*(1+i)**t
  return costo_opera

a_results = []
t_results = []
c_results = []

crescita=crescita/100
deficit=deficit/100
Costo_base=Costo_base*1000000000
i=i/100
pil=pil*1000000000
debito=debito*1000000000
apprendimento=apprendimento/100

for p in range(0,Progetti+0):
  tempo=round(t*(1-apprendimento)**p)
  costo=Costo_base*t*(1-apprendimento)**p
  a=costo_opera(i, tempo , costo)
  a_results.append(a)
  t_results.append(tempo)
  c_results.append(costo)


df = pd.DataFrame({'progetti': a_results,'Tempo':t_results, 'costo_netto':c_results})
df['Interessi']=df.progetti-df.costo_netto



import plotly.graph_objs as go

# Definire i dati da tracciare
trace = go.Scatter(x=df.index, y=df.progetti, mode='lines')

# Layout del grafico
layout = go.Layout(
    title=f'Costo complessivo per reattore <br> costo complessivo: {sum(df.progetti)/1000000000:.2f} mld € <br> Ipotesi: i={i}%, Tempo Foak ={t} anni, costo overnight FOAK  {Costo_base*t/1000000000:.2f} mld €',
    xaxis=dict(title='progetti realizzati'),
    yaxis=dict(title='costo in €')
)

# Creare la figura
costo = go.Figure(data=[trace], layout=layout)



# Mostrare il grafico
st.plotly_chart(costo)
# Creare le tracce per il grafico a barre
trace1 = go.Bar(x=df.index, y=df.costo_netto, name='Costo overnight')
trace2 = go.Bar(x=df.index, y=df.Interessi, name='Interessi', marker=dict(color='rgb(26, 118, 255)'),
                # 'rgb(26, 118, 255)' è il colore blu predefinito di Plotly
                # Puoi cambiare il colore a tuo piacimento
                # Ad esempio: 'rgb(255, 0, 0)' per il rosso
                #             'rgb(0, 255, 0)' per il verde
                #             ecc.
                )

# Creare il layout del grafico
layout = go.Layout(
    title=f'Scomposizione costo complessivo per reattore <br> costo medio: {sum(df.progetti)/1000000000/Progetti:.2f} mld € <br> Ipotesi: i={i}%, Tempo Foak ={t} anni, costo overnight FOAK  {Costo_base*t/1000000000:.2f} mld €',
    xaxis=dict(title='progetti realizzati'),
    yaxis=dict(title='costo in €'),
    barmode='stack'  # Impostare 'stack' per impilare le barre
)

# Creare la figura
fig = go.Figure(data=[trace1, trace2], layout=layout)

# Mostrare il grafico
st.plotly_chart(fig)

df['Quote']=df.progetti/df.Tempo
df['start']=1
df['Partenza']=partenza+df.start.shift(1).cumsum()
df.loc[0, 'Partenza'] = partenza

df['Conclusione']=df['Partenza']+df.Tempo

df['Partenza'] = df['Partenza'].fillna(0)
new_dfs = []
for _, row in df.iterrows():
    start_year = int(row['Partenza'])
    end_year = int(row['Conclusione'])
    year_range = range(start_year, end_year)  # Aggiungo 1 per includere anche l'anno di conclusione
    project_df = pd.DataFrame({
        'Anno': year_range,
        'Progetti':row['progetti']/row['Tempo'],
        'Interessi':row['Interessi']/row['Tempo'],
        'Costo_netto': row['costo_netto']/row['Tempo'],
        'Quote': row['Quote'],
        'Avanzamento':1/row['Tempo']
    })
    new_dfs.append(project_df)

# Concatenare tutti i nuovi dataframe in uno solo
result_df = pd.concat(new_dfs, ignore_index=True)



df_def=result_df.groupby('Anno').agg({
    'Quote':sum,
    'Progetti':sum,
    'Interessi':sum,
    'Costo_netto':sum,
    'Avanzamento':sum

})
df_def.Avanzamento=df_def.Avanzamento.cumsum()


# Creare le tracce per il grafico a barre
trace1 = go.Bar(x=df_def.index, y=df_def.Costo_netto, name='Costo overnight')
trace2 = go.Bar(x=df_def.index, y=df_def.Interessi, name='Interessi', marker=dict(color='rgb(26, 118, 255)'),
                # 'rgb(26, 118, 255)' è il colore blu predefinito di Plotly
                # Puoi cambiare il colore a tuo piacimento
                # Ad esempio: 'rgb(255, 0, 0)' per il rosso
                #             'rgb(0, 255, 0)' per il verde
                #             ecc.
                )

# Creare il layout del grafico
layout = go.Layout(
    title=f'Andamento costi dal {partenza} <br> Costo complessivo: {sum(df.progetti)/1000000000:.2f} mld € <br> Ipotesi: i={i}%, Tempo Foak ={t} anni, costo overnight FOAK  {Costo_base*t/1000000000:.2f} mld €',
    xaxis=dict(title='Anno'),
    yaxis=dict(title='Costo in €'),
    barmode='stack'  # Impostare 'stack' per impilare le barre
)

# Creare la figura
fig = go.Figure(data=[trace1, trace2], layout=layout)

# Mostrare il grafico
st.plotly_chart(fig)


df_def['Pil']=pil*(1+crescita)**(df_def.index-partenza-1)
df_def['Debito']=debito*(1+deficit-crescita)**(df_def.index-partenza-1)
df_def['DebitoPIL']=df_def['Debito']/df_def['Pil']
df_def['Debito1']=(debito+df_def['Quote'].cumsum())*(1+deficit-crescita)**(df_def.index-partenza-1)
df_def['Pilcontributo']=df_def['Avanzamento'].astype(int)/Progetti
df_def['Pil1']=(pil+df_def['Costo_netto']*0.5)*(1+crescita+(df_def['Pilcontributo']*0.4/100))**(df_def.index-partenza-1)
df_def['DebitoPIL1']=df_def['Debito1']/df_def['Pil1']
df_def['CreacitaPIL']=df_def['Pil']/df_def['Pil'].shift(1)-1
df_def['CreacitaPIL1']=df_def['Pil1']/df_def['Pil1'].shift(1)-1


# Creare le tracce per il grafico a linee
trace1 = go.Scatter(x=df_def.index, y=df_def.DebitoPIL*100, mode='lines', name='FMI')
trace2 = go.Scatter(x=df_def.index, y=df_def.DebitoPIL1*100, mode='lines', name='Modello stupido')

# Creare il layout del grafico
layout = go.Layout(
    title=f'Rapporto Debito Pil dal {partenza} <br> Costo complessivo: {sum(df.progetti)/1000000000:.2f} mld € <br> Ipotesi: i={i}%, Tempo Foak ={t} anni, costo overnight FOAK  {Costo_base*t/1000000000:.2f} mld €. <br> Ipotesi macro: crescita annuale media = {crescita*100}%, deficit annuale medio = {deficit*100}% ',
    xaxis=dict(title='Anno'),
    yaxis=dict(title='Rapporto Debito Pil (%)')
)

# Creare la figura
fig = go.Figure(data=[trace1, trace2], layout=layout)

# Mostrare il grafico
st.plotly_chart(fig)
