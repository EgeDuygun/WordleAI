# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 23:52:07 2022

@author: egedu
"""


import numpy as np
import time

start = time.time()

all_words = """FISCH,TROTZ,BIRKE,RUFEN,NOBEL,FOKUS,KREUZ,ZANGE,WILLE,TRICK,IDOLE,DROGE,REGEL,DOHLE,HARFE,HOEHE,ZWANG,EULEN,HAGEL,SALAT,ALTER,WONNE,WANNE,HASEN,PUDEL,LEHRE,RADIO,WEIHE,DRAHT,WOVON,RIPPE,GASSE,RODEN,CLOWN,EISEN,ORTEN,SACHE,ERKER,SEIFE,SAEGE,KUFEN,LINKS,WIEGE,SIRUP,STOER,SENAT,MUSIK,ZILLE,LIMIT,NOTIZ,INFAM,WUNDE,TAUFE,WULST,FLUOR,TEXTE,HOBBY,MUMIE,LEUTE,ASSEL,ELITE,VIDEO,ABTEI,PFUND,GUMMI,BOHNE,TITEL,PROSA,MADEN,TRIEB,SPEER,ELEVE,GABEN,ZUTUN,KASSE,GROLL,BIRNE,LUNTE,MEILE,ORGEL,HACKE,SKALA,GRAMM,DELLE,STICH,EUTER,GRUBE,URALT,SINNE,TOTAL,JAGEN,VENUS,TADEL,BREIT,ERPEL,LUNGE,HOSEN,SUPPE,ARTIG,SORTE,HINZU,WORAN,ERBSE,REIHE,BRACH,GENIE,FEIGE,MARKE,SELIG,START,MESSE,BONUS,APRIL,SAKKO,WORUM,CHAOS,CHROM,FAUST,SILBE,GRILL,ALTAR,LOKAL,ESSIG,DRECK,WIPPE,BAUCH,KRISE,UMBAU,GUNST,HYMNE,BEIZE,RAUPE,ZUTAT,LOGIK,MILDE,LYRIK,TEMPO,SOMIT,WANGE,WENIG,DAHIN,UEBEN,HEGEN,ABZUG,FATAL,HINAB,REGIE,DIAET,STATT,UNTER,KOMMA,BLICK,SAHNE,GREIS,BINDE,JUROR,ZELLE,MANIE,HUMOR,PUSTE,STROM,QUALM,TANNE,WARUM,AUTOR,SEITE,MARKT,GRIMM,PFERD,SPITZ,RAPPE,STEIG,HAARE,KELLE,RISPE,HECKE,AHNEN,APART,COUCH,ILTIS,BISON,FASER,HERAN,KLEID,GAREN,LITER,REELL,QUIRL,KNABE,FAUNA,BERUF,BAUER,HAUBE,STAAT,FESCH,KLIMA,ZEHEN,RINDE,HALLE,VOGEL,DUENN,EKLAT,DISCO,VILLA,SZENE,FOEHN,NARBE,FELGE,RUMPF,LINDE,MINUS,RECHT,DUERR,ORDEN,OPFER,NEBEN,DAVON,ERSTE,FARBE,ZWIRN,ERNTE,MENGE,WALZE,STETS,KNAST,AUTOS,PAARE,EBENE,ESSEN,STOCK,BRETT,KOMIK,NYLON,AGENT,IRDEN,HEBEN,WOMIT,SIPPE,KARTE,TRIST,DRAMA,BARDE,GRIFF,DEKOR,MUTIG,LARVE,THESE,MALER,FAMOS,PRIMA,LAUTE,ASIAT,WOLLE,HAUCH,ANRUF,MAERZ,AUGEN,TOSEN,MAGER,ALBUM,GENAU,EILIG,LAUBE,BARKE,MONAT,ROSIG,LOIPE,LACHE,LEINE,BOGEN,RUHIG,SEKTE,WOGEN,DOGMA,INSEL,LIEGE,JOKER,DRALL,LEGAL,GEBEN,KUGEL,HEBEL,BEIGE,RAMPE,AXIAL,KARRE,ZWEIG,LEHEN,KRUMM,RACHE,NICHT,OELIG,JUWEL,BAHRE,LEFZE,THEMA,KEGEL,RIESE,IMMER,QUERE,BOTEN,NONNE,UNSER,PILZE,FEUER,NISSE,KREBS,NUDEL,KLANG,NETTO,FROST,KOPIE,WRACK,LINKE,BETON,NATUR,NELKE,GLEIS,WANZE,KEHLE,GALLE,SECHS,DATEI,WERTE,RENTE,ANGEL,BRAUE,MITTE,STARR,TREND,FOTOS,SPAET,ARMUT,LEHNE,STIEL,ANGST,MORAL,DEKAN,FABEL,BEINE,ZUNFT,FRUST,ETHIK,GLATT,WEICH,STAMM,OCHSE,MOLCH,MODER,BIBER,FRAGE,KRANK,LIPPE,MAUER,FEIND,HERAB,JETZT,KNALL,TITAN,BRISE,BOMBE,STIFT,SONNE,GABEL,EIFER,EBNEN,VIRUS,BEUTE,TREUE,GEHEN,TROLL,GROSS,FERNE,TONNE,STEIN,ZIEGE,HITZE,MINEN,KASSA,HORDE,AREAL,NAGEN,OSTEN,HILFE,ROETE,SAGEN,ERNST,SCHAM,BLUME,TORTE,DUNST,HECHT,AORTA,FEGEN,BOXEN,SAITE,PUPPE,PISTE,MANKO,LUCHS,FORUM,STURM,GARDE,BLOED,FRIST,STERN,GNADE,STUMM,ERDEN,RASCH,JUBEL,ZUDEM,ENDEN,ENKEL,SPASS,FLOTT,PANIK,HORST,INDEX,RODEL,SACHT,LOEWE,BRIEF,GEIGE,INNEN,HAGER,KOHLE,PFEIL,RASUR,LENDE,FRONT,PAKET,DOLCH,RUEBE,HENNE,KAMPF,ANMUT,LOBEN,DABEI,HEIDE,WORTE,PEGEL,STUFE,PERLE,STEIF,RUEDE,TRUPP,GLIED,REISE,DARUM,PIRAT,WOCHE,GAMBE,BLOND,WEBER,FOREN,ROSEN,MENSA,WIESO,ACRYL,ELEND,UNRAT,HEUTE,WUCHT,OHREN,SCHEU,EMPOR,PAUSE,RIEGE,PATER,KERBE,VIRAL,ABBAU,FAKIR,STIER,JAHRE,SOHLE,EICHE,SAUNA,MAGMA,SONDE,KRIMI,ATLAS,KANTE,SPATZ,KAPER,FALKE,GLANZ,LODEN,LAMPE,URBAN,FUNDE,HETZE,RASER,SPOTT,UMHER,SALBE,EITER,AXIOM,BUCHT,DEGEN,DAMIT,KROPF,LADEN,DARIN,TORUS,VOKAL,MODUS,FROMM,HIRSE,SEIDE,AESEN,HEXEN,BELEG,GENOM,KURVE,WITWE,AFFEN,MUEDE,MUERB,HOTEL,TOBEN,BLASS,EIGEN,DAHER,SEHNE,LILIE,KOMET,RUEGE,PARTY,KERZE,MALEN,KUNDE,QUARK,RASEN,SUPER,LOYAL,REUIG,ALPIN,SCHAU,FAZIT,YACHT,PROFI,WERKE,WAAGE,ORKAN,SCHAR,KANNE,TEICH,IRRIG,ZIVIL,GUETE,HEUER,TAUEN,PARAT,SERIE,VITAL,ZINKE,BOESE,FEDER,FLUGS,OLIVE,BANAL,WESPE,RITZE,FASAN,INDIZ,KAMIN,ZWERG,RUSSE,NADEL,HOBEL,PFOTE,LISTE,SPECK,TANGO,GANZE,SICHT,ATOLL,KIPPE,LESEN,WINDE,APFEL,FADEN,SALON,KLEIN,AKTEN,BLUSE,DINGE,SALVE,HERUM,DRAUF,WUCHS,LABEN,MILIZ,WEITE,ECHSE,MIXEN,MODAL,BERGE,MENUE,FINTE,SEHEN,BLASE,BEULE,KUNST,WAGEN,DAUER,RATEN,RADAU,BEVOR,ETWAS,CHLOR,ULKIG,EXTRA,RUBIN,MIETE,BASIS,CHILI,DOSIS,KODEX,TRUEB,PARTE,WENDE,BRAUN,ZUZUG,EINST,MEERE,STOLA,ZOTTE,KATER,GRUFT,FALLE,EITEL,FUENF,PATEN,HOLEN,JACKE,RUDER,GEBET,SPREU,JUNGE,QUOTE,ABRUF,LACHS,OPTIK,PFAND,VIKAR,MOBIL,HAUPT,BLIND,MILCH,LAGER,TRAGE,WIESE,FLINK,BRAUT,DAMPF,LAERM,KRACH,BANDE,ZIRKA,ZYSTE,BADEN,FALTE,TUMOR,PILOT,LEBER,ZUVOR,HUENE,ESCHE,ERBIN,HEFTE,BLATT,MOEWE,FEIER,HOCKE,PLATZ,TATEN,FUNKE,SORGE,ROUTE,LICHT,PUNKT,BIEST,GURTE,INTIM,WESTE,SALTO,ARTEN,SCHUH,MAPPE,ZUNGE,AKTIV,PFAHL,FERSE,SAEEN,KNIFF,GENUG,STOLZ,REIFE,UNTEN,SUMME,NEBEL,PRALL,TABAK,THRON,MAJOR,ORGIE,RESTE,SEGEL,REIME,PORTO,WOHIN,UMZUG,LUXUS,DURST,WITZE,ZEILE,BESEN,VATER,ACHSE,LOCKE,KLUFT,UMWEG,MOPED,ANKER,OEDEM,ANZUG,TENOR,WICHT,TINTE,POSSE,OBERE,EINIG,SPIEL,PAPST,TIGER,BAUEN,GICHT,SUCHE,MAGIE,EILEN,KUEHL,KAKAO,PFLUG,KNIEN,WEISE,MOTTO,PALME,WORIN,TULPE,BORTE,ATOME,KELCH,DANKE,SKALP,LANZE,WEBEN,EXAKT,GEGEN,IMMUN,STEIL,STOFF,SAMEN,ONKEL,OELEN,LINIE,ATMEN,NABEL,RABEN,MIXER,PAUKE,GENRE,KISTE,FOLIE,TOTEM,ZEBRA,STARK,ERBEN,DICKE,ZUMAL,WEIDE,BEUGE,WARTE,ANTUN,OBHUT,WELPE,KUPPE,VISUM,ADERN,EINEN,ZEUGE,TIEFE,PRISE,BULLE,BUCHE,SITTE,BEIDE,WOBEI,ROMAN,PRINZ,AROMA,RINGE,LIEBE,FORST,STUCK,KEULE,ETAGE,LEDIG,LUEGE,MASSE,SUMPF,WEHEN,LINSE,NASAL,ZENIT,ORGAN,MEIST,SCHUB,TAGEN,AGAPE,LOTSE,TRITT,ABEND,KLOTZ,RITUS,GURKE,POLAR,LEBEN,ROTOR,DAVOR,REGEN,MOTOR,TATZE,RILLE,MEUTE,KURSE,PINIE,KLICK,WURST,WILDE,STURZ,GERTE,ALGEN,TEUER,LESER,MIMIK,FINNE,DUESE,STAND,GERNE,ADLER,AHORN,ROBBE,RADAR,AMPEL,NACHT,DOGGE,POLKA,BEERE,SANFT,BISSE,HAFER,MILBE,DUELL,KASTE,SOWIE,IRREN,LASSO,MODEM,PLATT,FUGEN,DACHS,KEHRE,WARAN,EDIKT,WEILE,NOTAR,KONTO,COACH,UNGUT,BEBEN,DIELE,NAEHE,DICHT,HANDY,IMKER,SATAN,INDEM,SPORT,MEISE,JAUSE,BETEN,STAUB,NOTEN,BASAR,CHAOT,REGAL,PANNE,PROBE,MULDE,WATTE,EIMER,FLAIR,HAFEN,SCHAF,EKZEM,UHREN,TUETE,FRUEH,HALDE,KEKSE,GUSTO,DECKE,STALL,POKAL,KNICK,SAMBA,TAUBE,HUNDE,KIOSK,UNFUG,KRAFT,ZINNE,PIXEL,FUTUR,ROHRE,ALARM,DRILL,KLAGE,EISIG,WIDER,SENKE,LEISE,DRUCK,BRUCH,BIWAK,MATTE,MAGEN,HUPEN,ALIAS,VORNE,KNAPP,SPALT,NEFFE,ABGAS,TROTT,HALLO,POKER,FIRMA,RAUTE,ZACKE,LATTE,FAHNE,UNART,ALIBI,VLIES,TRAKT,LEIER,DAUNE,SPORN,TAFEL,HAKEN,FRECH,REICH,WETTE,LABIL,WARZE,BIBEL,BROTE,TROSS,PACHT,VIOLA,BACHE,STAHL,DRANG,ZWECK,SONST,REDEN,FOYER,FLACH,LASER,MAKEL,KERNE,ZECHE,RUDEL,TIERE,WESEN,RINNE,GEBOT,FEILE,WEGEN,DEICH,BORKE,BLECH,KAUEN,FLUCH,QUASI,KEIME,ABTUN,ZIELE,BACKE,WACHS,ARMEE,LAUCH,PAPPE,RASSE,BOOTE,DUETT,ZOBEL,UEBEL,FLOSS,NAGEL,FLUSS,PLAGE,KAMEL,WADEN,KNOPF,SPULE,GATTE,TASSE,GESTE,CELLO,TEILE,ORBIT,METTE,TISCH,HAEME,LAUGE,SEGEN,KAESE,TRAUM,TARIF,LOSEN,BUBEN,STUTE,WAFFE,STOPP,LANGE,SERUM,FOLGE,ENZYM,FREMD,ECKEN,LEERE,BITTE,FLECK,BLANK,DATIV,PLANE,BUERO,KREIS,KLAUE,VOTUM,STADT,KADER,PILLE,MASKE,AKTIE,GRUEN,IDIOT,MACKE,MUELL,MACHT,FILME,TROST,EMSIG,EHREN,KANAL,WATEN,OPIUM,SENIL,SOGAR,RUHEN,BLITZ,ENORM,HURRA,ARENA,HABEN,MOTTE,URBAR,FIDEL,WIRTE,ENTEN,FIGUR,BIENE,SENSE,SPION,DARAN,PIZZA,DEPOT,KLAMM,FESTE,AEHRE,BRAND,STROH,GEIER,PEDAL,MOTIV,SEILE,DUMPF,NIERE,LAUNE,ULKEN,SOCKE,GRUND,METER,BANGE,ROLLE,TYPEN,WOHER,ENGEL,KRASS,JEHER,MANGO,PASTA,SAUER,DELTA,WUEST,MIENE,BEZUG,TANTE,BRUST,WAISE,STIRN,IKONE,WACHE,OTTER,IDEEN,AMSEL,THEKE,HIRTE,KATZE,SALDO,ZECKE,ZWIST,BARON,EINER,SCHAL,IDEAL,UNMUT,KRANZ,ACKER,FEHDE,WEDER,UEBER,KRAUS,NOVUM,KLOSS,ASCHE,FARCE,NACKT,RUINE,KAPPE,HUMAN,SEELE,DOCHT,KRONE,PUDER,MACHO,FAHRT,TALER,WERFT,BOXER,SUITE,STUHL,DUENE,KANON,LEDER,MUEHE,LURCH,PREIS,PLUMP,BRITE,OFFEN,TOAST,KUEHN,HERDE,RAUCH,GOTIK,TRANK,ALPEN,KABEL,KETTE,DURCH,SESAM,MODUL,ZITAT,LABOR,KUTTE,TASTE,GEIST,GRELL,ANBAU,HAUEN,BLOCK,VORAN,RATTE,GELSE,INNIG,HALME,DOSEN,STILL,BELAG,SEHER,WELLE,EKELN,FUCHS,SCHON,OZEAN,SUCHT,FRACK,PSALM,KRAUT,ALLEE,TEILS,ECKIG,BODEN,ZUCHT,ANTIK,DEMUT,KURIE,DAMEN,LEGEN,PHASE,PONYS,HONIG,WOLKE,UNION,PRUNK,STUBE,VORAB,PUMPE,BUSCH,DATUM,JEANS,RUNDE,RISSE,KRIEG"""

answers = all_words.lower().split(",")


def get_class(word, target):
    
    word = word.lower()
    output = ""
    
    for i in range(len(word)):
        if word[i] not in target:
            output += "b"
        elif word[i] == target[i]:
            output += "g"
        else:
            output += "y"
            
    return output


def get_entropy(word, current_list):
    
    probs = {}
    
    for i in current_list:
        word_class = get_class(word,i)        
        if word_class not in probs:
            probs[word_class] = 1/len(current_list)
        else:
            probs[word_class] += 1/len(current_list)
            
    entropy = 0
    
    for k in probs:
        entropy += probs[k] * (-np.log2(probs[k]))
    
    return entropy



def narrow_list(guess, output, current_list):
    
    l_form = output.split()
    s_form = set(l_form)
    
    
    if len(s_form) == len(output):    
    
        for i in range(len(output)):
            
            if output[i] == "g":       
                for j in current_list[:]:
                    if guess[i] != j[i]:
                        current_list.remove(j)
            
            elif output[i] == "b":
                for j in current_list[:]:
                    if guess[i] in j:
                        current_list.remove(j)
                        
            else:
                for j in current_list[:]:
                    if (guess[i] not in j) or (guess[i] == j[i]):
                        current_list.remove(j)
                        
    else:
        
        for i in range(len(guess)):
            cnt = guess.count(guess[i])
            
            if cnt == 1:
                
                if output[i] == "g":       
                    for j in current_list[:]:
                        if guess[i] != j[i]:
                            current_list.remove(j)
                
                elif output[i] == "b":
                    for j in current_list[:]:
                        if guess[i] in j:
                            current_list.remove(j)
                            
                else:
                    for j in current_list[:]:
                        if (guess[i] not in j) or (guess[i] == j[i]):
                            current_list.remove(j)
                            
            else:
                strng = ""              
                    
                for j in range(len(guess)):
                    
                    if (guess[i] == guess[j]):
                        strng += output[j]
                    else:
                        strng += "_"
                        
                #print(strng)
                    
                if (strng.count("b") == cnt):
                    for j in current_list[:]:
                        if guess[i] in j:
                            current_list.remove(j)
                            
                elif ("b" in strng) and ("g" in strng):
                    idx = strng.find("g")
                    for j in current_list[:]:
                        if (guess[idx] != j[idx]):
                            current_list.remove(j)
                            
                elif ("b" in strng) and ("y" in strng):
                    idx = strng.find("y")
                    for j in current_list[:]:
                        if (guess[idx] not in j):
                            current_list.remove(j)
                            
    return current_list
                    

def prediction(curr_list):
    
    entropies = {}
    
    for i in curr_list:
        entropies[i] = get_entropy(i, curr_list)
        
    sorted_ent = sorted(entropies.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_ent


pred = prediction(answers)

print("Your set of first guesses should be:", pred[0:10])

guess = 0

while True:    
    
    
    pred = str(input("What is your answer?: ")).lower() 
    
    if len(pred) != 5 or (pred not in answers):
        while True:
            pred = str(input("Please make a valid guess!: ")).lower() 
            if len(pred) == 5 and (pred in answers):
                break
        
    guess += 1
    inp = str(input("What is the current response (in terms of g = green, y = yellow, b = black): ")).lower()  
    
    if inp == "ggggg":
        print("Congratulations! The word was '"+ str(pred)+ "' and you have found it in", guess,"trials!")
        break

    
    
    answers.remove(pred)
    answers = narrow_list(guess = pred, output = inp, current_list = answers)
    
    pred_list = prediction(answers)

    print("Your new guess should be:", pred_list)

    


end = time.time()

print("It took this seconds:", end-start)
