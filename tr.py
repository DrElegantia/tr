#spoiler allert


import pandas as pd
import streamlit as st
import plotly.graph_objs as go

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

modello = st.radio(
    "Che profilo vuoi impostare al tuo modello?",
    ["conservativo", "best case scenario", "worst case scenario",  'Zollino',"Azzecca", "personalizza modello"], help="Selezionando un modello verranno valorizzati in modo automatico i vari parametri, questi verranno riportati nei singoli grafici. Se si preferisce agira autonomamente nella modifica dei parametri è sufficiente selezionare l'opzione per personalizzare il modello")

if modello == "conservativo":
    i = 4
    t = 15

    Progetti = 26
    partenza = 2024
    apprendimento = 3
    Costo_base =  1.0

    occupati_diretti = 1000

    occupati_indiretti = 66
    pil_diretti = 100
    pil_indiretti = 50
    pil_eco = 1

    taglio =  0
elif modello == "Zollino":
    i = 4
    t = 9

    Progetti = 26
    partenza = 2024
    apprendimento = 1
    Costo_base =  0.6

    occupati_diretti = 1000

    occupati_indiretti = 66
    pil_diretti = 100
    pil_indiretti = 50
    pil_eco = 1

    taglio =  0
elif modello == "Azzecca":
    i = 10
    t = 7

    Progetti = 26
    partenza = 2024
    apprendimento = 2
    Costo_base =  0.8

    occupati_diretti = 1000

    occupati_indiretti = 66
    pil_diretti = 100
    pil_indiretti = 50
    pil_eco = 1

    taglio =  0

elif modello == "best case scenario":
    i = 4
    t = 10

    Progetti = 26
    partenza = 2024
    apprendimento = 3
    Costo_base = 1.0

    occupati_diretti = 1200

    occupati_indiretti = 70
    pil_diretti = 100
    pil_indiretti = 100
    pil_eco = 2

    taglio = 1
elif modello == "worst case scenario":
    i = 7
    t = 20

    Progetti = 26
    partenza = 2024
    apprendimento = 3
    Costo_base = 1.0

    occupati_diretti = 1200

    occupati_indiretti = 50
    pil_diretti = 100
    pil_indiretti = 0
    pil_eco = 2

    taglio = 0


elif modello=="personalizza modello":

    i = st.slider(
        'Che tasso di  interesse prevedi per il costo del debito?',
        4, 20,4, help="Il tasso di interesse influenza il costo complessivo dell'operazione")
    t = st.slider(
        'In quanto tempo stimi venga realizzato il FOAK?',
        4, 30,7, help="FOAK=First-of-A-Kind, ovvero il primo reattore realizzato. Il tempo dei successivi reattori è dato dal tempo del FOAK e dal tasso di apprendimento. Il modello è realizzato in modo da far partire un reattore ogni anno.")
    apprendimento = st.slider(
        'Che tasso di apprendimento stimi? Se negativo, il tasso va ad aumentare tempi di realizzo e costi.',
        -10, 10,3,help="Il tasso di apprendimento stima la curva di apprendimento che si prevede avrà il progetto. Il tasso per il modello avrà effetto sia sul tempo di realizzazione che sul costo con pari entità")
    Progetti = st.slider(
        'Su quanti reattori vuoi basare il modello?',
        1, 30,26,help="Il modello si basa sull'ipotesi che tutti i reattori appartengano allo stesso tipo")
    partenza = 2024

    Costo_base=st.slider(
        'Quanto stimi possa ammontare il costo overnight del FOAK annualmente? Seleziona un vsalore in miliardi di €',
        0.6, 5.0,1.0, help="Il costo overnight rappresenta il costo complessivo per realizzare il reattore, al netto degli interessi, per comodità qui viene espresso annualmente. ")

    occupati_diretti=st.slider(
        f'A quanto ammonta la stima di occupazione diretta per reattore? Selezionare il numero di occupati per reattore',
        500, 1200,1000, help="Il PIL viene stimato attraveso l'occupazione per il valore aggiunto dato da ogni occupato diretto. Il numero di occupati è valorizzato in base allo stato di avanzamento del progetto")

    occupati_indiretti=st.slider(
        f'Quanti occupati indiretti per occupato diretto per singolo reattore? Seleziona la percentuale di occupati indiretti per occupati diretti',
        0, 100,66, help="Il PIL viene stimato attraveso l'occupazione per il valore aggiunto dato da ogni occupato diretto. Il numero di occupati è valorizzato in base allo stato di avanzamento del progetto")
    pil_diretti=st.slider(
        f"Quanto valore aggiunto prevedi che possa generare un dipendente diretto nel settore dell'energia nucleare, rispetto alla media nazionale?",
        0, 150,100, help="Ogni occupato diretto genera un valore aggiunto la cui sommatoria può essere una buona stima del PIL")

    pil_indiretti=st.slider(
        f"Quanto valore aggiunto prevedi che possa generare un dipendente indiretto nel settore dell'energia nucleare, rispetto alla media nazionale?",
        0, 100,50, help="Ogni occupato diretto genera un valore aggiunto la cui sommatoria può essere una buona stima del PIL")
    pil_eco=st.slider(
        f"Si prevede un aumento della produttività per occupato dell'intera economia grazie all'adozione dell'energia nucleare, rispetto alla produttività senza energia nucleare, alla fine del progetto?",
        0, 100,1, help="Il PIL oltre ad aumentare per effetto dell'occupazione diretta e indiretta aggiuntiva, può aumentare a seguito della migliorata produttività dell'economia grazie al cambiamento tecnologico. Qui è possibile valorizzare un coefficiente che andrà a moltiplicare il valore aggiunto per occupato dell'intera economia.")

    genre = st.radio(
        "Vuoi che il modello preveda un taglio della spesa pensionistica?",
        ["No", "dell'1% di pil", "del 2% del pil"], help='Sulla base delle stime RGS il modello calcola la spesa epnsionistica, è possibile ridurre il suo impatto sui conti pubblici di alcuni punti di pil attraverso la selezione multipla.')

    if genre == "No":
        taglio=0
    elif genre == "dell'1% di pil":
        taglio=1
    elif genre == "del 2% del pil":
        taglio = 2


def costo_opera(i, t, co):
  costo_opera=co*(1+i)**t
  return costo_opera

a_results = []
t_results = []
c_results = []
occupati_indiretti=occupati_indiretti/100

Costo_base=Costo_base*1000000000
i=i/100

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


import pandas as pd

# Dati originali
data = {
    'Anno': [2015, 2020, 2025, 2030, 2035, 2040, 2045, 2050, 2055, 2060, 2065, 2070],

    'Popolazione [20-64]': [35.941, 35.184, 34.142, 32.906, 31.203, 29.330, 27.732, 26.730, 25.994, 25.353, 24.716, 23.940],

    'Popolazione totale': [60.295, 59.641, 58.560, 57.906, 57.185, 56.370, 55.395, 54.165, 52.630, 50.906, 49.213, 47.722],
    'Tasso di occupazione [15-64]': [56.0, 57.5, 61.1, 61.9, 63.0, 64.0, 64.6, 64.8, 64.9, 64.9, 64.9, 65.0],
    'PIL reale (mld di € 2015)': [1.655, 1.574, 1.809, 1.879, 1.933, 1.994, 2.059, 2.146, 2.248, 2.355, 2.461, 2.564],
    'Numero totale di pensionati (mgl)': [15.200, 14.761, 15.035, 15.705, 16.306, 16.959, 17.316, 17.108, 16.483, 15.766, 15.038, 14.390],
    'Importo medio di pensione (€ 2015)': [13851, 15058, 15229, 15411, 15699, 15880, 16005, 16120, 16434, 17155, 18396, 19917],
    'Spesa pensionistica/PIL': [15.6, 16.9, 16.1, 16.4, 16.8, 17.0, 17.0, 16.2, 15.2, 14.6, 14.3, 14.3]
}

popolazione = pd.DataFrame(data)

# Creazione del DataFrame con tutti gli anni desiderati
anni_desiderati = pd.DataFrame({'Anno': range(2015, 2071)})

# Merge dei DataFrame per avere tutti gli anni con i relativi dati
popolazione_anni_completi = pd.merge(anni_desiderati, popolazione, on='Anno', how='left')

# Riempimento dei vuoti interpolando i dati
popolazione_anni_completi_interpolati = popolazione_anni_completi.interpolate(method='linear', axis=0)

pop=popolazione_anni_completi_interpolati
pop['Numero occupati di 15−64 anni']=pop['Tasso di occupazione [15-64]']*pop['Popolazione [20-64]']*10000
pop['PIL per occupato di 15−64 anni']=(pop['PIL reale (mld di € 2015)']*1000000000000)/(pop['Numero occupati di 15−64 anni'])

df_def=result_df.groupby('Anno').agg({
    'Quote':sum,
    'Progetti':sum,
    'Interessi':sum,
    'Costo_netto':sum,
    'Avanzamento':sum

})
df_def.Avanzamento=df_def.Avanzamento.cumsum()
# Unione dei DataFrame 'df_def' e 'pop' sulla colonna 'Anno'
df_def = df_def.merge(pop, on='Anno', how='left')


def calculate_avanzamento_app(avanzamento):
    if avanzamento % 1 != 0:
        return int(avanzamento)+1
    else:
        return int(avanzamento)

df_def['Avanzamento_app'] = df_def['Avanzamento'].apply(calculate_avanzamento_app)
df_def.at[df_def.index[-1], 'Avanzamento_app'] = Progetti


df_def['Stima pil RGS']=df_def['PIL per occupato di 15−64 anni']*df_def['Numero occupati di 15−64 anni']
df_def['Numero addetti diretti nucleare']=occupati_diretti*df_def['Avanzamento_app']
df_def['Numero addetti indiretti nucleare']=df_def['Numero addetti diretti nucleare']*occupati_indiretti
df_def['Numero occupati di 15−64 anni mp']=df_def['Numero addetti diretti nucleare']+df_def['Numero addetti indiretti nucleare']+df_def['Numero occupati di 15−64 anni']
df_def['PIL per addetto diretto modello']=df_def['PIL per occupato di 15−64 anni']*(1+pil_diretti/100)
df_def['PIL per addetto indiretto modello']=df_def['PIL per occupato di 15−64 anni']*(1+pil_indiretti/100)
df_def['PIL diretto nucleare']=df_def['PIL per addetto diretto modello']*df_def['Numero addetti diretti nucleare']
df_def['PIL indiretto nucleare']=df_def['PIL per addetto indiretto modello']*df_def['Numero addetti indiretti nucleare']
df_def['PIL aggiuntivo nucleare']=df_def['PIL diretto nucleare']+df_def['PIL indiretto nucleare']
df_def['PIL modello nucleare']=df_def['PIL aggiuntivo nucleare']+df_def['Stima pil RGS']*(1+pil_eco*df_def['Avanzamento_app']/Progetti/100)
df_def['Stima crescita pil RGS']=(df_def['Stima pil RGS']/df_def['Stima pil RGS'].shift(1)-1)*100
df_def['Stima crescita pil Nucleare']=(df_def['PIL modello nucleare']/df_def['PIL modello nucleare'].shift(1)-1)*100

# Creare le tracce per il grafico a linee
trace1 = go.Scatter(x=df_def['Anno'], y=df_def['PIL modello nucleare'], mode='lines', name='stima pil')
trace2 = go.Scatter(x=df_def['Anno'], y=df_def['Stima pil RGS'], mode='lines', name='pil rgs')

# Creare il layout del grafico
layout = go.Layout(
    title='Confronto Stima PIL',
    xaxis=dict(title='Anno'),
    yaxis=dict(title='Stima PIL')
)

# Creare la figura
fig = go.Figure(data=[trace1, trace2], layout=layout)

# Mostrare il grafico
st.plotly_chart(fig)

df_def['Redditi da lavoro dipendente']=df_def['Stima pil RGS']*0.08
df_def['Consumi_intermedi']=df_def['Stima pil RGS']*0.05
df_def['Altre prestazioni sociali']=df_def['Stima pil RGS']*0.05
df_def['Spesa pensionistica']=(df_def['Spesa pensionistica/PIL']-taglio)*df_def['Stima pil RGS']/100
df_def['Altre spese correnti']=df_def['Stima pil RGS']*0.03
df_def['Interessi passivi']=df_def['Stima pil RGS']*0.035
df_def['Totale spese in conto capitale']=df_def['Stima pil RGS']*0.035

df_def['Spese']=df_def['Spesa pensionistica']+df_def['Totale spese in conto capitale']+df_def['Altre spese correnti']+df_def['Interessi passivi']+df_def['Redditi da lavoro dipendente']+df_def['Redditi da lavoro dipendente']+df_def['Altre prestazioni sociali']+df_def['Consumi_intermedi']


df_def['Entrate dirette']=df_def['Stima pil RGS']*0.16
df_def['Entrate indirette']=df_def['Stima pil RGS']*0.15
df_def['Entrate in conto capitale']=df_def['Stima pil RGS']*0.001
df_def['Entrate contributi']=df_def['Stima pil RGS']*0.15
df_def['Entrate altre']=df_def['Stima pil RGS']*0.04
df_def['Entrate altre non tributarie']=df_def['Stima pil RGS']*0.01
df_def['Entrate']=df_def['Entrate dirette']+df_def['Entrate indirette']+df_def['Entrate in conto capitale']+df_def['Entrate contributi']+df_def['Entrate altre']+df_def['Entrate altre non tributarie']
df_def['Debito'] = df_def['Stima pil RGS'] * 140/100
df_def['Indebitamento netto']=df_def['Entrate']-df_def['Spese']
df_def['Debito'] = - df_def['Indebitamento netto'].cumsum() + df_def['Debito'].shift(1)
df_def['Spese con nucleare']=df_def['Spese']+df_def['Quote']
df_def['Entrate con nucleare']=df_def['Entrate']+df_def['PIL aggiuntivo nucleare']*0.5
df_def['Indebitamento netto con nucleare']=df_def['Entrate con nucleare']-df_def['Spese con nucleare']
df_def['Debito con nucleare'] = df_def['Stima pil RGS'] * 140/100
df_def['Debito con nucleare'] = - df_def['Indebitamento netto con nucleare'].cumsum() + df_def['Debito con nucleare'].shift(1)

# Calcola il rapporto debito/PIL e debito nucleare/PIL per ogni anno
rapporto_debito_pil = df_def['Debito'] / df_def['Stima pil RGS']
rapporto_debito_nucleare_pil = df_def['Debito con nucleare'] / df_def['PIL modello nucleare']

# Creare le tracce per il grafico a linee
trace1 = go.Scatter(x=df_def['Anno'], y=rapporto_debito_pil, mode='lines', name='Debito/Pil')
trace2 = go.Scatter(x=df_def['Anno'], y=rapporto_debito_nucleare_pil, mode='lines', name='Debito/Pil nucleare')

# Creare il layout del grafico
layout = go.Layout(
    title='Rapporto Debito/PIL',
    xaxis=dict(title='Anno'),
    yaxis=dict(title='Rapporto Debito/PIL')
)

# Creare la figura
fig = go.Figure(data=[trace1, trace2], layout=layout)

# Mostrare il grafico
st.plotly_chart(fig)

# Creare le tracce per il grafico a linee
trace1 = go.Scatter(x=df_def['Anno'], y=df_def['Stima crescita pil RGS'], mode='lines', name='crescita rgs')
trace2 = go.Scatter(x=df_def['Anno'], y=df_def['Stima crescita pil Nucleare'], mode='lines', name='crescita stima pazzerella')

# Creare il layout del grafico
layout = go.Layout(
    title='Stima Crescita PIL',
    xaxis=dict(title='Anno'),
    yaxis=dict(title='Stima Crescita PIL')
)

# Creare la figura
fig = go.Figure(data=[trace1, trace2], layout=layout)

# Mostrare il grafico
st.plotly_chart(fig)

# Creare le tracce per il grafico a linee
trace1 = go.Scatter(x=df_def['Anno'], y=df_def['Indebitamento netto']/df_def['Stima pil RGS']*100, mode='lines', name='Indebitamento netto')
trace2 = go.Scatter(x=df_def['Anno'], y=df_def['Indebitamento netto con nucleare']/df_def['PIL modello nucleare']*100, mode='lines', name='Indebitamento netto con nucleare')

# Creare il layout del grafico
layout = go.Layout(
    title='Indebitamento Netto',
    xaxis=dict(title='Anno'),
    yaxis=dict(title='Indebitamento Netto')
)

# Creare la figura
fig = go.Figure(data=[trace1, trace2], layout=layout)

# Mostrare il grafico
st.plotly_chart(fig)
