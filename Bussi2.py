from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

# # Tarkoitukseni on tehdä laskuri siten, että kyseistä laskuria voi käyttää vaikka tiet tai linja muuttuisi 
# # jollakin tavalla. Kuitenkin, koska optimointialgoritmien käyttö ei ollut tehtävässä sallittua, olen rajannut
# # muokattavuutta käyttäen seuraavaa lisäoletusta:

# # Jokaiseen määränpäähän pääsee optimiajassa vaihtamalla bussia enintään kaksi kertaa.


pysakit= [
   "A",
   "B",
   "C",
   "D",
   "E",
   "F",
   "G",
   "H",
   "I",
   "J",
   "K",
   "L",
   "M",
   "N",
   "O",
   "P",
   "Q",
   "R"
 ] 
   
tiet = [
   {
     "mista": "A",
     "mihin": "B",
     "kesto": 3
   },
   {
     "mista": "B",
     "mihin": "D",
     "kesto": 2
   },
   {
     "mista": "D",
     "mihin": "A",
     "kesto": 1
   },
   {
     "mista": "A",
     "mihin": "C",
     "kesto": 1
   },
   {
     "mista": "C",
     "mihin": "D",
     "kesto": 5
   },
   {
     "mista": "C",
     "mihin": "E",
     "kesto": 2
   },
   {
     "mista": "E",
     "mihin": "D",
     "kesto": 3
   },
   {
     "mista": "E",
     "mihin": "F",
     "kesto": 1
   },
   {
     "mista": "F",
     "mihin": "G",
     "kesto": 1
   },
   {
     "mista": "G",
     "mihin": "H",
     "kesto": 2
   },
   {
     "mista": "H",
     "mihin": "I",
     "kesto": 2
   },
   {
     "mista": "I",
     "mihin": "J",
     "kesto": 1
   },
   {
     "mista": "I",
     "mihin": "G",
     "kesto": 1
   },
   {
     "mista": "G",
     "mihin": "K",
     "kesto": 8
   },
   {
     "mista": "K",
     "mihin": "L",
     "kesto": 1
   },
   {
     "mista": "L",
     "mihin": "M",
     "kesto": 1
   },
   {
     "mista": "E",
     "mihin": "M",
     "kesto": 10
   },
   {
     "mista": "M",
     "mihin": "N",
     "kesto": 2
   },
   {
     "mista": "N",
     "mihin": "O",
     "kesto": 2
   },
   {
     "mista": "O",
     "mihin": "P",
     "kesto": 2
   },
   {
     "mista": "O",
     "mihin": "Q",
     "kesto": 1
   },
   {
     "mista": "P",
     "mihin": "Q",
     "kesto": 2
   },
   {
     "mista": "N",
     "mihin": "Q",
     "kesto": 1
   },
   {
     "mista": "Q",
     "mihin": "R",
     "kesto": 5
   },
   {
     "mista": "R",
     "mihin": "N",
     "kesto": 3
   },
   {
     "mista": "D",
     "mihin": "R",
     "kesto": 6
   }

 ]

linjastot = {
   "keltainen": ["E", "F", "G", "K", "L", "M", "N"],
   "punainen": ["C", "D", "R", "Q", "N", "O", "P"],
   "vihreä": ["D", "B", "A", "C", "E", "F", "G", "H", "I", "J"],
   "sininen": ["D", "E", "M", "N", "O"]
 }







#Palauttaa tien pituuden, jos solmujen a ja b välillä on suora tie
def road_distance(a,b):
    road_length = 0
    for i in range(len(tiet)):
        if (tiet[i]['mista'] == a or tiet[i]['mihin']==a) and (tiet[i]['mista'] == b or tiet[i]['mihin']==b):
            road_length = tiet[i]['kesto']
    
    return road_length




### Määrittää listojen lst1 ja lst2 yhteiset pisteet ja palauttaa tiedot listana
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 


#Katsoo mitkä linjat kulkevat annetun pisteen 'point' kautta. Palauttaa listana vaihtoehdot.
def find_lines(point):
    point_lines =[None]*4
    s=0
    for i in linjastot:
        if point in linjastot[i]:
            point_lines[s]=i
            s=s+1
    
    #### Palautetaan arvot ilman None: arvoja
    point_lines2= [None]*s
    for i in range(0,s):
        point_lines2[i]=point_lines[i]
    return point_lines2



#                                        ##################################
########################################## LASKURIT: COUNT_DISTANCE 1,2,3 ###########################
#                                        ##################################  
        
        
#Lasketaan etäisyys kahden pisteen välillä, kun koko matka matkustetaan samalla linjalla. 
#Funktio saa parametreikseen alku- sekä loppupisteen ja käytettävän linjan i. 
#AE: Alku ja loppupisteen on kuuluttava linjnan i reitille, ja oltava start != end
def count_distance(start, end, i):
    start_index  = linjastot[i].index(start)
    end_index    = linjastot[i].index(end)
    new_distance = 0
        
    if start_index >  end_index : #(Tilanne: (H,I,end,A,start))
        while start_index > end_index :
            new_distance  = road_distance(linjastot[i][start_index],linjastot[i][start_index-1]) + new_distance
            start_index   = start_index -1

    
    else:
        while start_index < end_index: #(Tilanne: (H, start, I, A , end))
            new_distance  = road_distance(linjastot[i][start_index],linjastot[i][start_index+1]) + new_distance
            start_index   = start_index +1  
            
        
    return new_distance



#Lasketaan etäisyys kahden pisteen välillä, kun käytetään täsmälleen kahta linjaa. Funktio saa parametreikseen
#alku- sekä loppupisteen ja käytettävät linjat. 
#AE: start kuuluu i linjaan ja end j linjaan, i != j  #### Onko enää näin?
def count_distance_two(start,end,i,j):
    change_point   = []
    common_points  = intersection(linjastot[i],linjastot[j]) #Kahden linjan yhteiset solmupisteet

    if start in common_points: #Hylätään kuitenkin alkupisteet ja loppupisteet
        index_start = common_points.index(start)
        common_points.pop(index_start)
    if end in common_points:
        index_end = common_points.index(end)
        common_points.pop(index_end)

    best_distance = 3000
  
    
    #Käydään läpi niin kauan, kunnes kaikki linjanvaihtopisteet on käyty läpi
    while len(common_points) != 0:  
      point = common_points[0]

      total_distance      = count_distance(start, point, i) + count_distance(point, end, j)
      if total_distance < best_distance:
        best_distance = total_distance
        change_point  = [point]
      elif total_distance == best_distance:
        change_point.append(point)


      common_points.pop(0)             
                                                      

    return  [best_distance, change_point]     




#Lasketaan etäisyys kahden pisteen välillä, kun käytetään täsmälleen kolmea linjaa. Funktio saa parametreikseen
#alku- sekä loppupisteen. Funktio palauttaa parhaat reitit listana [reitti1, reitti2,...], jossa
#reitti = [matkanKesto, käytettävät linjat, vaihtopiste1, vaihtopiste2]. Lisäksi vaihtopiste on lista,
#joka sisältää kaikki mahdolliset vaihtopisteet, joissa kyseisellä optimireitillä voi linjaa vaihtaa 
#kun kaikki muut muuttujat pysyvät vakiona. 
#ESIM: Optimireitti (B -> M) on siis:
#alkupiste --> linja1 -> vaihtopiste1 ->  linja2 -> vaihtopiste2 -> linja3    --> loppu
#   B      --> vihreä ->      D       -> sininen ->   E tai M    -> keltainen --> L
def count_distance_three(start,end):
    #current_point = start
    start_lines    = find_lines(start)  #Linjat, jotka kulkevat alkupisteen kautta
    end_lines      = find_lines(end)    #Linjat, jotka kulkevat loppupisteen kautta
    best_distance  = 4000       #Paras etäisyys
    final_result   = [None]*4   #Parhaan reitin tiedot  =[best_distance, best_lines, change_line1, change_line2],
                                #jossa change_line kertoo vaihtopysäkin 

    alt_result     = [None]*4   #Vaihtoehtoisesti parhaan reitin tiedot
    list_of_best_results = []   #Lista kaikista parhaista reiteistä
    

    for busA in start_lines:  #Linjat joilla pääsee alkupisteestä
        for busB in linjastot: #Linjat joihin vaihdetaan   (*****)
            if busA != busB: #Ei vaihdeta samaan bussiin

                for node in linjastot[busB]: #Käydään läpi jokainen solmu, jossa voidaan vaihtaa bussiin B (*****)
                    if node in linjastot[busA] and node != start: #Kulkeeko bussi A tämän solmun kautta (jonka kautta bussi B  kulkee)
                                                                  #Lisäksi lähtöpisteessä ei saa vaihtaa bussia
                        
                        for busC in end_lines:  #Käydään läpi jokainen linja, jolla pääsee määränpäähän.
                            if busB != busC:  # Ei vaihdeta samaan bussiin
                                distanceA    = count_distance(start, node, busA)
                                mid_result   = count_distance_two(node, end, busB, busC)  ##int
                                new_distance = distanceA + mid_result[0]
                                

                            
                                if new_distance < best_distance: # Tallennetaan, jos löydettiin parempi reitti
                                    final_result    = [None]*4
                                    best_distance   = new_distance

                                    final_result[0] = new_distance
                                    final_result[1] = [busA, busB, busC]
                                    final_result[2] = [node]
                                    final_result[3] = mid_result[1]
                                    list_of_best_results = [final_result]

                                    ##Lista list_of_best_results on lopulta muotoa  [  final_result1, final_result2, final_result3 ... ],
                                    ##koska else-kohdassa tuloksia voidaan saada lisää

                                
                                elif new_distance == best_distance: ### Tallennetaan yhtä hyvä, vaihtoinen reitti
                                  alt_result= [None]*4
                                  alt_result[0] = new_distance
                                  alt_result[1] = [busA, busB, busC]
                                  alt_result[2] = [node]
                                  alt_result[3] = mid_result[1]
                                  list_of_best_results.append(alt_result)
                                  
                                  
                                
    return list_of_best_results


#                       #########               ########              ########           ########
######################### MAIN ################## MAIN ################ MAIN ############# MAIN ############              
#                       #########               ########              ########           ########
def main(start, end):

  #Lähtöpaikka start 
  #Määränpää end 
  best_distance= 3000 #nopeimman reitin arvo
  best_lines=[None]*3 #Listaa optimireitin käytettävät linjat järjestyksessä

  change_point = []

  #final_result  == [kesto, linjat, vaihtopiste1, vaihtopiste2] Kuvaa yksittäistä tulosta
  list_of_best_results =[] ###  ==[final_result1, final_result2, ...],  Kuvaa kokonaistulosta

  start_lines = find_lines(start) #Alkupisteestä liikkuvat linjat
  end_lines   = find_lines(end)  #Loppupisteessä liikkuvat linjat


######## Lasketaan paras reitti, kun käytetään täsmälleen yhtä linjaa
  for i in start_lines: 
    if start in end_lines:
      new_distance = count_distance(start,end, i)
      
      if best_distance > new_distance: ### Tallennetaan reitin tulokset, jos parempi arvo löydetään
        best_distance = new_distance

        final_result = [new_distance, [i], [], []]  ### final_result muotoa [kesto, linjat, vaihtopiste1, vaihtopiste2]
        list_of_best_results = [final_result]

      
      elif best_distance == new_distance: ### Jos löydetty reitti on kestoltaan yhtä hyvä, tallennetaan myös se
        other_result = [new_distance, [i] ,[], []]
        list_of_best_results.append(other_result)




########## Lasketaan paras reitti, kun käytetään täsmälleen kahta linjaa

  for i in start_lines: #Alkupisteestä liikkuvat linjat
    for j in end_lines: #Loppupisteessä liikkuvat linjat

      if i != j:
        result_list  = count_distance_two(start, end, i, j)
        new_distance = result_list[0] 

        if best_distance > new_distance: ### Tallennetaan reitin tulokset, jos parempi arvo löydetään
          best_distance = new_distance
          best_lines    = [i,j]
          change_point  = result_list[1]
          final_result = [best_distance, best_lines, change_point ,[]]
          list_of_best_results = [final_result]
          
        
        elif best_distance == new_distance: ### Jos löydetty reitti on kestoltaan yhtä hyvä, tallennetaan myös se
          best_distance = new_distance
          best_lines    = [i,j]
          change_point  = result_list[1]
          other_result  = [best_distance, best_lines, change_point ,[]]
          list_of_best_results.append(other_result)



######### Lasketaan paras reitti, kun käytetään täsmälleen kolmea linjaa
  result_list = count_distance_three(start,end)  
  
  new_distance = result_list[0][0]
  if best_distance > new_distance: ### Tallennetaan reitin tulokset, jos parempi arvo löydetään
    best_distance = new_distance
    list_of_best_results = result_list


  elif best_distance == new_distance: ### Jos löydetty reitti on kestoltaan yhtä hyvä, tallennetaan myös se
    
    index = 0
    while index < len(result_list):
      list_of_best_results.append(result_list[index])
      index = index +1


  # Palautus:
  # list_of_best_results = [ result1, result2, ..., ], jossa
  # result = [etäisyys, linjat, vaihtopiste1, vaihtopiste2]
  return list_of_best_results

   


@app.route('/')
def front_page():
    return render_template('index.html' )



@app.route('/result-page', methods=['GET', 'POST'])
def result_page():
    try:
      start   = request.form['start_location'].upper()
      end     = request.form['end_location'].upper()
      results = main(start, end)
      kesto   = results[0][0]
      linjat  = [results[i][1] for i in range(0, len(results))] ## listana linjavaihtoehdot [tulos1 linjat, tulos2 linjat ...]
      vaihto1 = [results[i][2] for i in range(0, len(results))] 
      vaihto2 = [results[i][3] for i in range(0, len(results))] 
      vaihtoehdotLKM = len(results)

    
      return render_template('result.html', 
                            kesto = kesto,
                            linjat = linjat,
                            vaihto1 = vaihto1,
                            vaihto2 = vaihto2,
                            start = start, 
                            end = end,
                            vaihtoehdotLKM = vaihtoehdotLKM )
    except:
      error = True
      return render_template('index.html', error = error)
