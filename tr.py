#spoiler allert


import pandas as pd
import streamlit as st
import plotly.graph_objs as go

st.title('Il modello più semplicistico di analisi dei costi del nucleare')
st.header('Nuclear is :blue[cool] :sunglasses:', divider='rainbow')
st.write("Questa app è stata creata da [Umberto Bertonelli](https://umbertobertonelli.it).")
st.write("La documentazione completa è disponibile [qui](https://github.com/DrElegantia/femminicidi_italia/tree/main).")
st.divider()

st.write("Questo applicativo è uno strumento che permette agli utenti di stimare i costi e il tempo di realizzazione di un progetto di energia nucleare. Il modello è basato su alcuni parametri, come il tasso di interesse, il tempo di realizzazione, il costo base annuale del progetto, il tasso di apprendimento e il numero di reattori da basare il modello. Il programma permette di scegliere l'anno di partenza del progetto e i tassi di crescita e deficit economici del paese senza nucleare. Il modello fornisce risultati in forma di grafici, tra cui uno che mostra il costo complessivo del progetto in relazione al numero di progetti realizzati, e un altro che mostra l'andamento del costo nel tempo. Il modello ha delle limitazioni, come la mancanza di considerazione di fattori come la variabilità dei costi di capitale e operativi, la capacità di gestire il rischio e la sicurezza, e la capacità di integrare il nucleare con altre fonti di energia rinnovabili. Tuttavia, il modello è utile per fornire una stima grossolana iniziale dei costi e del tempo di realizzazione di un progetto di energia nucleare.")

st.write("Se si vuole approfondire il tema attraverso documenti e opinione di esperti, qui trovate un'intervista al prof. Jacopo Buongiorno, Direttore del Centro per i sistemi avanzati di energia nucleare al MIT")
# URL del video su YouTube
video_url = "https://youtu.be/FOqnCk1Uv7I"

# Incorpora il video nella tua app Streamlit
st.video(video_url)

st.divider()
pluto=False
agree = st.checkbox('Sono consapevole dei limiti del modello')
if agree:
    agree_2 = st.checkbox('Sono consapevole che, come ogni modello, anche questo è errato')
    if agree_2:
        agree_3 = st.checkbox('Sono consapevole che le risposte del modello dipendono dalle ipotesi che io andrò a selezionare, oltre che dalla struttura dello stesso')
        if agree_3:

            modello = st.radio(
                "Che profilo vuoi impostare al tuo modello?",
                [ 'BEST CASE SCENARIO',"SCENARIO MEDIANO", 'TASSI BASSI', 'SUPER APPRENDIEMNTO', "WORST CASE SCENARIO",'SMR' ,"PERSONALIZZA MODELLO"], help="Selezionando un modello verranno valorizzati in modo automatico i vari parametri, questi verranno riportati nei singoli grafici. Se si preferisce agira autonomamente nella modifica dei parametri è sufficiente selezionare l'opzione per personalizzare il modello")

            if modello == "SCENARIO MEDIANO":
                i = 4
                t = 12

                Progetti = 26
                partenza = 2026
                apprendimento = 1.5
                Costo_base =  8.0

                occupati_diretti = 600
                occupati_indiretti = 33
                occupati_costruzione=2200
                occupati_indotto =66
                pil_diretti = 100
                pil_indiretti = 33
                pil_costruzione=10
                pil_indotto = -10
                pil_eco = 1

                taglio =  0



            if modello == "TASSI BASSI":
                i = 2
                t = 12

                Progetti = 26
                partenza = 2026
                apprendimento = 1.5
                Costo_base =  8.0

                occupati_diretti = 600
                occupati_indiretti = 33
                occupati_costruzione=2200
                occupati_indotto =66
                pil_diretti = 100
                pil_indiretti = 33
                pil_costruzione=10
                pil_indotto = -10
                pil_eco = 1

                taglio =  0

            if modello == "SMR":
                i = 2
                t = 5

                Progetti = 50
                partenza = 2026
                apprendimento = 4
                Costo_base = 3.5

                occupati_diretti = 150
                occupati_indiretti = 33
                occupati_costruzione=500
                occupati_indotto = 75
                pil_diretti = 100
                pil_indiretti = 33
                pil_costruzione=10
                pil_indotto = -10
                pil_eco = 5

                taglio =  0
                pluto=True


            if modello == "SUPER APPRENDIMENTO":
                i = 4
                t = 12

                Progetti = 26
                partenza = 2026
                apprendimento = 3.5
                Costo_base =  8.0

                occupati_diretti = 600
                occupati_indiretti = 33
                occupati_costruzione=2200
                occupati_indotto =66
                pil_diretti = 100
                pil_indiretti = 33
                pil_costruzione=10
                pil_indotto = -10
                pil_eco = 1

                taglio =  0


            elif modello == "BEST CASE SCENARIO":
                i = 3
                t = 7

                Progetti = 32
                partenza = 2026
                apprendimento = 2.5
                Costo_base =  5.0

                occupati_diretti = 900
                occupati_indiretti = 40
                occupati_costruzione=2200
                occupati_indotto =75
                pil_diretti = 150
                pil_indiretti = 50
                pil_costruzione=30
                pil_indotto = 15
                pil_eco = 5

                taglio =  0
            elif modello == "WORST CASE SCENARIO":
                i = 6
                t = 16

                Progetti = 8
                partenza = 2026
                apprendimento = 0.5
                Costo_base =  8.0

                occupati_diretti = 500
                occupati_indiretti = 33
                occupati_costruzione=2200
                occupati_indotto =50
                pil_diretti = 100
                pil_indiretti = 33
                pil_costruzione=10
                pil_indotto = -20
                pil_eco = 0

                taglio =  0


            elif modello=="PERSONALIZZA MODELLO":

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
                    1, 35,26,help="Il modello si basa sull'ipotesi che tutti i reattori appartengano allo stesso tipo")
                partenza = 2026

                Costo_base=st.slider(
                    'Quanto stimi possa ammontare il costo overnight del FOAK? Seleziona un valore in miliardi di €',
                    0.5, 20.0,10.0, help="Il costo overnight rappresenta il costo complessivo per realizzare il reattore, al netto degli interessi ")
                occupati_costruzione = st.slider(
                    f'A quanto ammonta la stima di occupati/anno per la costruzione del reattore?',
                    1000, 2500, 1800,
                    help="Il PIL viene stimato attraveso l'occupazione per il valore aggiunto dato da ogni occupato (diretto, indiretto e fase di costruzione). Il numero di occupati è valorizzato in base allo stato di avanzamento del progetto")
                occupati_diretti=st.slider(
                    f"A quanto ammonta la stima di occupati/anno per l'operativià del reattore?",
                    300, 900,600, help="Il PIL viene stimato attraveso l'occupazione per il valore aggiunto dato da ogni occupato diretto. Il numero di occupati è valorizzato in base allo stato di avanzamento del progetto")

                occupati_indiretti=st.slider(
                    f'A quanto ammonta la stima di occupati/anno indiretti rispetto agli occupati/anno diretti (costruzione + operatività)?',
                    0, 100,33, help="Il PIL viene stimato attraveso l'occupazione per il valore aggiunto dato da ogni occupato diretto. Il numero di occupati è valorizzato in base allo stato di avanzamento del progetto")

                occupati_indotto=st.slider(
                    f'A quanto ammonta la stima di occupati/anno indotto rispetto agli occupati/anno diretti e indiretti?',
                    0, 100,66, help="Il PIL viene stimato attraveso l'occupazione per il valore aggiunto dato da ogni occupato diretto. Il numero di occupati è valorizzato in base allo stato di avanzamento del progetto")

                pil_costruzione=st.slider(
                    f"Quanto valore aggiunto prevedi che possa generare un dipendente nella fase di costruzione del reattore in più (o in meno) rispetto alla media nazionale?",
                    -100, 100,10, help="Ogni occupato (diretto, indiretto, nella fase di costruzione) genera un valore aggiunto la cui sommatoria può essere una buona stima del PIL")

                pil_diretti=st.slider(
                    f"Quanto valore aggiunto prevedi che possa generare un dipendente diretto nel settore dell'energia nucleare in più (o in meno) rispetto alla media nazionale?",
                    0, 150,100, help="Ogni occupato diretto genera un valore aggiunto la cui sommatoria può essere una buona stima del PIL")

                pil_indiretti=st.slider(
                    f"Quanto valore aggiunto prevedi che possa generare un dipendente indiretto nel settore dell'energia nucleare in più (o in meno) rispetto alla media nazionale?",
                    -100, 100,10, help="Ogni occupato diretto genera un valore aggiunto la cui sommatoria può essere una buona stima del PIL")
                pil_indotto=st.slider(
                    f"Quanto valore aggiunto prevedi che possa generare un dipendente indotto nel settore dell'energia nucleare in più (o in meno) rispetto alla media nazionale?",
                    -100, 100,-10, help="Ogni occupato diretto genera un valore aggiunto la cui sommatoria può essere una buona stima del PIL")
                pil_eco=st.slider(
                    f"Si prevede un aumento della produttività nel settore dell'industria ed energia grazie all'adozione dell'energia nucleare, alla fine del progetto?",
                    0, 100,5, help="Il PIL oltre ad aumentare per effetto dell'occupazione diretta e indiretta aggiuntiva, può aumentare a seguito della migliorata produttività dell'economia grazie al cambiamento tecnologico. Qui è possibile valorizzare un coefficiente che andrà a moltiplicare il valore aggiunto per occupato dell'intera economia.")

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


            Costo_base=Costo_base*1000000000
            i=i/100

            apprendimento=apprendimento/100

            for p in range(0,Progetti+0):
              tempo=round(t*max((1-apprendimento)**p,0.3))
              costo=Costo_base*max((1-apprendimento)**p,0.3)
              a=costo_opera(i, tempo, costo)
              a_results.append(a)
              t_results.append(tempo)
              c_results.append(costo)


            df = pd.DataFrame({'progetti': a_results,'Tempo':t_results, 'costo_netto':c_results})
            df['Interessi']=df.progetti-df.costo_netto






            # Creare le tracce per il grafico a barre
            trace1 = go.Bar(x=df.index, y=df.costo_netto, name='Costo Overnight', marker=dict(color='#1A76FF'))
            trace2 = go.Bar(x=df.index, y=df.Interessi, name='Costo di Finanziamento', marker=dict(color='#84C9FF'))


            # Creare il layout del grafico
            layout = go.Layout(
                title=f'Costo dell\'n-esimo reattore scomposto in <span style="color:#1A76FF;">OVERNIGHT</span> e <span style="color:#84C9FF;"> DI FINANZIAMENTO</span> <br> Costo medio di 1 reattore: {sum(df.progetti)/1000000000/Progetti:.2f} mld €<br> Ipotesi: i={i*100:.2f}%, apprendimento={apprendimento*100:.2f}%, Tempo FOAK={t} anni, costo overnight FOAK={Costo_base/1000000000:.2f} mld €',
                xaxis=dict(title='Progetto Realizzato'),
                yaxis=dict(title='Costo in €'),
                barmode='stack',  # Impostare 'stack' per impilare le barre
                showlegend=False
            )

            # Creare la figura
            fig = go.Figure(data=[trace1, trace2], layout=layout)

            # Mostrare il grafico
            st.plotly_chart(fig)

            df['Quote']=df.progetti/df.Tempo
            df['start']=1
            df['Partenza']=partenza+df.start.shift(1).cumsum()
            if pluto==True:
                df['Partenza']=round(partenza+df.start.shift(1).cumsum()/3)
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
                    'Avanzamento':1/row['Tempo'],
                    'start':row['start']
                })
                new_dfs.append(project_df)

            # Concatenare tutti i nuovi dataframe in uno solo
            result_df = pd.concat(new_dfs, ignore_index=True)



            df_def=result_df.groupby('Anno').agg({
                'Quote':sum,
                'Progetti':sum,
                'Interessi':sum,
                'Costo_netto':sum,
                'Avanzamento':sum,
                'start':sum

            })
            df_def.Avanzamento=df_def.Avanzamento.cumsum()


            # Creare le tracce per il grafico a barre
            trace1 = go.Bar(x=df_def.index, y=df_def.Costo_netto, name='Costo overnight', marker=dict(color='#1A76FF'))
            trace2 = go.Bar(x=df_def.index, y=df_def.Interessi, name='Costo di finanziamento', marker=dict(color='#84C9FF'))



            # Creare il layout del grafico
            layout = go.Layout(
                title=f'Andamento delle spese annuali, scomposte in <span style="color:#1A76FF;">OVERNIGHT</span> e <span style="color:#84C9FF;">DI FINANZIAMENTO</span> <br> Spesa media annuale: {(df_def.Costo_netto.mean()+df_def.Interessi.mean())/1000000000:.2f} mld € <br> Ipotesi: i={i*100:.2f}%, apprendimento={apprendimento*100:.2f}%, Tempo FOAK = {t} anni, costo overnight FOAK={Costo_base/1000000000:.2f} mld €',
                xaxis=dict(title='Anno'),
                yaxis=dict(title='Costo in €'),
                barmode='stack',
                showlegend=False
            )

            # Creare la figura
            fig = go.Figure(data=[trace1, trace2], layout=layout)

            # Mostrare il grafico
            st.plotly_chart(fig)

            # Creare le tracce per il grafico a barre
            trace1 = go.Bar(x=df_def.index, y=df_def.Costo_netto.cumsum(), name='Costo overnight', marker=dict(color='#1A76FF'))
            trace2 = go.Bar(x=df_def.index, y=df_def.Interessi.cumsum(), name='Costo di finanziamento', marker=dict(color='#84C9FF'))



            # Creare il layout del grafico
            layout = go.Layout(
                title=f'Andamento della spesa cumulata, scomposta in <span style="color:#1A76FF;">OVERNIGHT</span> e <span style="color:#84C9FF;">DI FINANZIAMENTO</span> <br> Spesa complessiva: {(df_def.Costo_netto.sum()+df_def.Interessi.sum())/1000000000:.2f} mld € <br> Ipotesi: i={i*100:.2f}%, apprendimento={apprendimento*100:.2f}%, Tempo FOAK={t} anni, costo overnight FOAK={Costo_base/1000000000:.2f} mld €',
                xaxis=dict(title='Anno'),
                yaxis=dict(title='Costo in €'),
                barmode='stack',
                showlegend=False
            )

            # Creare la figura
            fig = go.Figure(data=[trace1, trace2], layout=layout)

            # Mostrare il grafico
            st.plotly_chart(fig)



            # Dati originali
            data = {
                'Anno': [2015, 2020, 2025, 2030, 2035, 2040, 2045, 2050, 2055, 2060, 2065, 2070],
                'Popolazione [20-54]': [28.337, 26.753, 24.942, 23.533, 22.474, 21.683, 20.876, 20.167, 19.518, 18.862, 18.161, 17.547],
                'Popolazione [55-64]': [7.604, 8.431, 9.200, 9.373, 8.730, 7.647, 6.857, 6.563, 6.476, 6.491, 6.554, 6.393],
                'Popolazione totale': [60.295, 59.641, 58.560, 57.906, 57.185, 56.370, 55.395, 54.165, 52.630, 50.906, 49.213, 47.722],
                'PIL reale (mld di € 2015)': [1.655, 1.574, 1.809, 1.882, 1.939, 2.005, 2.076, 2.170, 2.279, 2.395, 2.508, 2.614],
                'Spesa pensionistica/PIL': [15.6, 16.9, 16.1, 16.4, 16.8, 17, 16.8, 16.1, 15.1, 14.4, 14.1, 14.1],
                'Numero di occupati': [22.121, 22.385, 23.737, 23.972, 23.597, 22.828, 21.891, 21.315, 20.951, 20.639, 20.269, 19.847]
            }

            popolazione = pd.DataFrame(data)
            popolazione['Popolazione [20-64]']=popolazione['Popolazione [20-54]']+popolazione['Popolazione [55-64]']

            # Creazione del DataFrame con tutti gli anni desiderati
            anni_desiderati = pd.DataFrame({'Anno': range(2015, 2071)})

            # Merge dei DataFrame per avere tutti gli anni con i relativi dati
            popolazione_anni_completi = pd.merge(anni_desiderati, popolazione, on='Anno', how='left')

            # Riempimento dei vuoti interpolando i dati
            popolazione_anni_completi_interpolati = popolazione_anni_completi.interpolate(method='linear', axis=0)

            pop=popolazione_anni_completi_interpolati
            pop['Numero occupati di 15−64 anni']=pop['Numero di occupati']*1000000
            pop['PIL per occupato di 15−64 anni']=(pop['PIL reale (mld di € 2015)']*1000000000000)/(pop['Numero occupati di 15−64 anni'])

            df_def=result_df.groupby('Anno').agg({
                'Quote':sum,
                'Progetti':sum,
                'Interessi':sum,
                'Costo_netto':sum,
                'Avanzamento':sum,
                'start':sum

            })
            df_def.Avanzamento=df_def.Avanzamento.cumsum()
            df_def['end'] = df_def.index.map(lambda x: (df['Conclusione'] < x).sum())
            # Unione dei DataFrame 'df_def' e 'pop' sulla colonna 'Anno'
            df_def = df_def.merge(pop, on='Anno', how='left')



            df_def['Avanzamento_app'] = df_def['Avanzamento'].astype(int)
            df_def.at[df_def.index[-1], 'Avanzamento_app'] = Progetti
            # Dati in lavoratori annui per reattore


            df_def['Stima pil RGS']=df_def['PIL per occupato di 15−64 anni']*df_def['Numero occupati di 15−64 anni']
            df_def['Numero costruttori nucleare']=df_def['start']*occupati_costruzione
            df_def['Numero addetti ope nucleare']=occupati_diretti*df_def['end']
            df_def['Numero addetti indiretti nucleare']=df_def['Numero addetti ope nucleare']*occupati_indiretti/100+df_def['Numero costruttori nucleare']*occupati_indiretti/100
            df_def['Numero addetti indotti nucleare']=df_def['Numero addetti ope nucleare']*occupati_indotto/100+df_def['Numero costruttori nucleare']*occupati_indotto/100+df_def['Numero addetti indiretti nucleare']*occupati_indotto/100


            df_def['Numero occupati di 15−64 anni nucleare']=df_def['Numero addetti ope nucleare']+df_def['Numero addetti indiretti nucleare']+df_def['Numero occupati di 15−64 anni']+df_def['Numero costruttori nucleare']+df_def['Numero addetti indotti nucleare']


            df_def['PIL per costruttori nucleare']=df_def['Numero costruttori nucleare']*(1+pil_costruzione/100)*df_def['PIL per occupato di 15−64 anni']

            df_def['PIL per addetto ope nucleare']=df_def['Numero addetti ope nucleare']*(1+pil_diretti/100)*df_def['PIL per occupato di 15−64 anni']

            df_def['PIL per addetto indiretto nucleare']=df_def['Numero addetti indiretti nucleare']*(1+pil_indiretti/100)*df_def['PIL per occupato di 15−64 anni']
            df_def['PIL per addetto indotto nucleare'] = df_def['Numero addetti indiretti nucleare'] * (1 + pil_indotto / 100)*df_def['PIL per occupato di 15−64 anni']


            df_def['PIL aggiuntivo nucleare']=df_def['PIL per addetto ope nucleare']+df_def['PIL per addetto indiretto nucleare']+df_def['PIL per costruttori nucleare']+df_def['PIL per addetto indotto nucleare']
            df_def['PIL modello nucleare']=df_def['PIL aggiuntivo nucleare']+df_def['Stima pil RGS']*(1+pil_eco*df_def['end']/Progetti*0.25/100)
            df_def['Stima crescita pil RGS']=(df_def['Stima pil RGS']/df_def['Stima pil RGS'].shift(1)-1)*100
            df_def['Stima crescita pil Nucleare']=(df_def['PIL modello nucleare']/df_def['PIL modello nucleare'].shift(1)-1)*100

            # Creare le tracce per il grafico a linee
            trace1 = go.Scatter(x=df_def['Anno'], y=df_def['PIL modello nucleare'], mode='lines', name='PIL - Stima modello Nucleare', marker=dict(color='#1A76FF'))
            trace2 = go.Scatter(x=df_def['Anno'], y=df_def['Stima pil RGS'], mode='lines', name='PIL - Stima RGS - Scenario nazionale base',marker=dict(color='#FF0000'))

            # Creare il layout del grafico
            layout = go.Layout(
                title='Andamento del PIL confronto fra <br> <span style="color:#FF0000;">RGS - SCENARIO NAZIONALE BASE</span> e <span style="color:#1A76FF;">STIMA MODELLO NUCLEARE</span>',
                xaxis=dict(title='Anno'),
                yaxis=dict(title='Stima PIL'),
                showlegend=False
            )

            # Creare la figura
            fig = go.Figure(data=[trace2, trace1], layout=layout)

            # Mostrare il grafico
            st.plotly_chart(fig)

            df_def['Redditi da lavoro dipendente']=df_def['Stima pil RGS']*0.08
            df_def['Consumi_intermedi']=df_def['Stima pil RGS']*0.05
            df_def['Altre prestazioni sociali']=df_def['Stima pil RGS']*0.05
            df_def['Spesa pensionistica']=(df_def['Spesa pensionistica/PIL']-taglio)*df_def['Stima pil RGS']/100
            df_def['Altre spese correnti']=df_def['Stima pil RGS']*0.03
            df_def['Interessi passivi']=df_def['Stima pil RGS']*0.04
            df_def['Totale spese in conto capitale']=df_def['Stima pil RGS']*0.035

            df_def['Spese']=df_def['Spesa pensionistica']+df_def['Totale spese in conto capitale']+df_def['Altre spese correnti']+df_def['Interessi passivi']+df_def['Redditi da lavoro dipendente']+df_def['Redditi da lavoro dipendente']+df_def['Altre prestazioni sociali']+df_def['Consumi_intermedi']


            df_def['Entrate dirette']=df_def['Stima pil RGS']*0.15
            df_def['Entrate indirette']=df_def['Stima pil RGS']*0.15
            df_def['Entrate in conto capitale']=df_def['Stima pil RGS']*0.001
            df_def['Entrate contributi']=df_def['Stima pil RGS']*0.15
            df_def['Entrate altre']=df_def['Stima pil RGS']*0.04
            df_def['Entrate altre non tributarie']=df_def['Stima pil RGS']*0.01
            df_def['Entrate']=df_def['Entrate dirette']+df_def['Entrate indirette']+df_def['Entrate in conto capitale']+df_def['Entrate contributi']+df_def['Entrate altre']+df_def['Entrate altre non tributarie']


            df_def['Indebitamento netto']=df_def['Entrate']-df_def['Spese']
            df_def['Debito'] = - df_def['Indebitamento netto'].cumsum() + df_def.loc[0,'Stima pil RGS'] * 139/100
            df_def['Spese con nucleare']=df_def['Spese']+df_def['Quote']
            df_def['Entrate con nucleare']=df_def['Entrate']+df_def['PIL aggiuntivo nucleare']*0.45
            df_def['Indebitamento netto con nucleare']=df_def['Entrate con nucleare']-df_def['Spese con nucleare']

            df_def['Debito con nucleare'] = - df_def['Indebitamento netto con nucleare'].cumsum() + df_def.loc[0,'Stima pil RGS'] * 139/100

            # Calcola il rapporto debito/PIL e debito nucleare/PIL per ogni anno
            rapporto_debito_pil = df_def['Debito'] / df_def['Stima pil RGS']
            rapporto_debito_nucleare_pil = df_def['Debito con nucleare'] / df_def['PIL modello nucleare']

            # Creare le tracce per il grafico a linee
            trace1 = go.Scatter(x=df_def['Anno'], y=rapporto_debito_pil, mode='lines', name='RGS - SCENARIO NAZIONALE BASE', marker=dict(color='#FF0000'))
            trace2 = go.Scatter(x=df_def['Anno'], y=rapporto_debito_nucleare_pil, mode='lines', name='STIMA MODELLO NUCLEARE', marker=dict(color='#1A76FF'))

            # Creare il layout del grafico
            layout = go.Layout(
                title='Andamento del rapporto Debito / PIL, confronto fra <br> <span style="color:#FF0000;">RGS - SCENARIO NAZIONALE BASE</span> e <span style="color:#1A76FF;">STIMA MODELLO NUCLEARE</span>',
                xaxis=dict(title='Anno'),
                yaxis=dict(title='Rapporto Debito/PIL'),
                showlegend=False
            )

            # Creare la figura
            fig = go.Figure(data=[trace1, trace2], layout=layout)

            # Mostrare il grafico
            st.plotly_chart(fig)

            # Creare le tracce per il grafico a linee
            trace1 = go.Scatter(x=df_def['Anno'], y=df_def['Stima crescita pil RGS'], mode='lines', name='RGS - SCENARIO NAZIONALE BASE', marker=dict(color='#FF0000'))
            trace2 = go.Scatter(x=df_def['Anno'], y=df_def['Stima crescita pil Nucleare'], mode='lines', name='STIMA MODELLO NUCLEARE', marker=dict(color='#1A76FF'))

            # Creare il layout del grafico
            layout = go.Layout(
                title='Andamento crescita del PIL, confronto fra <br> <span style="color:#FF0000;">RGS - SCENARIO NAZIONALE BASE</span> e <span style="color:#1A76FF;">STIMA MODELLO NUCLEARE</span>',
                xaxis=dict(title='Anno'),
                yaxis=dict(title='Stima Crescita PIL'),
                showlegend=False
            )

            # Creare la figura
            fig = go.Figure(data=[trace1, trace2], layout=layout)

            # Mostrare il grafico
            st.plotly_chart(fig)

            # Creare le tracce per il grafico a linee
            trace1 = go.Scatter(x=df_def['Anno'], y=df_def['Indebitamento netto']/df_def['Stima pil RGS']*100, mode='lines', name='RGS - SCENARIO NAZIONALE BASE', marker=dict(color='#FF0000'))
            trace2 = go.Scatter(x=df_def['Anno'], y=df_def['Indebitamento netto con nucleare']/df_def['PIL modello nucleare']*100, mode='lines', name='STIMA MODELLO NUCLEARE', marker=dict(color='#1A76FF'))

            # Creare il layout del grafico
            layout = go.Layout(
                title='Andamento Indebitamento Netto in rapporto al PIL, confronto fra <br> <span style="color:#FF0000;">RGS - SCENARIO NAZIONALE BASE</span> e <span style="color:#1A76FF;">STIMA MODELLO NUCLEARE</span>',
                xaxis=dict(title='Anno'),
                yaxis=dict(title='Indebitamento Netto')
            )

            # Creare la figura
            fig = go.Figure(data=[trace1, trace2], layout=layout)

            # Mostrare il grafico
            st.plotly_chart(fig)

            # Creare le tracce per il grafico a linee
            trace1 = go.Scatter(x=df_def['Anno'], y=df_def['Numero costruttori nucleare'], mode='lines', name='Numero costruttori nucleare')
            trace2 = go.Scatter(x=df_def['Anno'], y=df_def['Numero addetti indiretti nucleare'], mode='lines', name='Numero addetti indiretti nucleare')
            trace3 = go.Scatter(x=df_def['Anno'], y=df_def['Numero addetti ope nucleare'], mode='lines', name='Numero addetti operatività nucleare')
            trace4 = go.Scatter(x=df_def['Anno'], y=df_def['Numero addetti indotti nucleare'], mode='lines', name='Numero addetti indotti nucleare')

            # Creare il layout del grafico
            layout = go.Layout(
                title='Occupazione nucleare',
                xaxis=dict(title='Anno'),
                yaxis=dict(title='Occupazione')
            )

            # Creare la figura
            fig = go.Figure(data=[trace1, trace2, trace3, trace4], layout=layout)

            # Mostrare il grafico
            st.plotly_chart(fig)


            import streamlit as st

            # Definizione del testo con le formule LaTeX
            latex_text = r"""
            La formula per calcolare il costo dell'operazione in base al tasso di interesse e al tempo di realizzazione è:
            
            $$
            costo\_opera = co \times (1 + i)^t
            $$
            
            dove:
            - $costo\_opera$ è il costo dell'operazione,
            - $co$ è il costo overnight,
            - $i$ è il tasso di interesse,
            - $t$ è il tempo di realizzazione.
            
            La formula per calcolare il tempo di realizzazione di un progetto in base al tasso di apprendimento è:
            
            $$
            tempo = t \times (1 - apprendimento)^p
            $$
            
            dove:
            - $tempo$ è il tempo di realizzazione del progetto,
            - $t$ è il tempo di realizzazione del FOAK (First-of-A-Kind),
            - $apprendimento$ è il tasso di apprendimento,
            - $p$ è il numero di progetti realizzati.
            
            La formula per calcolare il costo overnight di un progetto in base al tasso di apprendimento è:
            
            $$
            costo overnight = co FOAK \times (1 - apprendimento)^p
            $$
            
            dove:
            - $co FOAK$ è il costo overnight del FOAK (First-of-A-Kind),
            - $apprendimento$ è il tasso di apprendimento,
            - $p$ è il numero di progetti realizzati.
            
            
            
            La formula per calcolare il valore aggiunto per occupato è:
            
            $$
            valore\_aggiunto = occupati \times valore\_aggiunto\_per\_occupato
            $$
            
            dove:
            - $valore\_aggiunto$ è il valore aggiunto,
            - $occupati$ è il numero di occupati,
            - $valore\_aggiunto\_per\_occupato$ è il valore aggiunto per occupato.
            
            La formula per calcolare il PIL in base al valore aggiunto e al numero di occupati è:
            
            $$
            PIL = valore\_aggiunto \times occupati
            $$
            
            dove:
            - $PIL$ è il Prodotto Interno Lordo,
            - $valore\_aggiunto$ è il valore aggiunto,
            - $occupati$ è il numero di occupati.
            
            La formula per calcolare il PIL aggiuntivo del progetto nucleare è:
            
            $$
            PILn = VAnd \times Ond + VAni \times Oni+ VAnc \times Onc
            $$
            
            dove:
            - $PILn$ è il Prodotto Interno Lordo generato dal nucleare,
            - $VAnd$ è il valore aggiunto del singolo occupato diretto nel progetto nucleare,
            - $VAni$ è il valore aggiunto del singolo occupato indiretto nel progetto nucleare,
            - $VAnc$ è il valore aggiunto del singolo occupato nella fase di costruzione del progetto nucleare,
            - $Ond$ è il numero di occupati diretti nel progetto nucleare,
            - $Oni$ è il numero di occupati indiretti nel progetto nucleare,
            - $Onc$ è il numero di occupati nella fase di costuzione del progetto nucleare,
            """

            # Utilizzo di st.markdown() per renderizzare il testo formattato in Markdown



            with st.expander("Come abbiamo fatto i conti"):
                st.markdown(latex_text, unsafe_allow_html=True)
