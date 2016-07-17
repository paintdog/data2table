Die Funktionen im Modul data2table können genutzt werden, um einen wohl geformten Datenbestand in Tabellenform zu bringen. Die Daten in Tabellenform können dann in ein Wiki oder in eine Github-Readme-Seite eingefügt werden.

## Grundsätzliche Verwendung

Die Datenpflege in einer Tabelle im Markdown-Format ist mühsam und unübersichtlich. Um hier Abhilfe zu schaffen, werden die Daten auskommentiert einer Seite oberhalb der späteren Tabelle beigegeben:

> &lt;!-- Wechselkurs DM zu OstMark<br>
> Datenbasis für die nachfolgende Tabelle:<br><br>
> Jahr;DM;M;Wechselkurs;Kommentar<br>
> 1970;1;1,80;1 : 1,8;<br>
> 1975;1;2,20;1 : 2,2;<br>
> 1980;1;2,50;1 : 2,5;<br>
> 1987;1;4,00;1 : 4,0;<br>
> 1988;1;4,40;1 : 4,4;<br>
> 1989;1;5,00;1 : 5,0;Jahr der Wende<br>
> --&gt;

Die Pflege der Daten erfolgt dann im auskommentierten Datenbestand. Bei Bedarf wird aus diesem Datenbestand dann mittels den im Modul enthaltenen Funktionen eine neue, aktualisierte Tabelle erzeugt und auf der Seite eingefügt, wobei die veraltete Tabelle gelöscht wird.

Der Datenbestand kann so auch leicht in eine csv-Datei ausgelagert, mit Microsoft Excel oder LibreOffice Calc weiterverarbeitet und anschließend wieder auf der Seite gespeichert werden.

## data2table_wiki(data)

Der Funktion data2table_wiki(string) werden Daten als String übergeben. Die Funktion gibt dann in der Konsole die formatierte Tabelle in Wikisyntax aus. Eine grundlegende Formatierung wird vorgenommen.
```python
data = """Jahr;DM;M;Wechselkurs;Kommentar
1970;1;1,80;1 : 1,8;
1975;1;2,20;1 : 2,2;
1980;1;2,50;1 : 2,5;
1987;1;4,00;1 : 4,0;
1988;1;4,40;1 : 4,4;
1989;1;5,00;1 : 5,0;Jahr der Wende"""
    
data2table_wiki(data)
```

Ergibt dann fertig im Wiki:

![Das Bild kann nicht angezeigt werden.](https://raw.githubusercontent.com/paintdog/data2table/master/wiki_tabelle.png "Ergebnis im Wiki (MediaWiki)")

Aktuell gibt es keine Einstellmöglichkeiten. Spalten mit einer führenden Zahl werden automatisch rechtsbündig ausgerichtet. Die Daten in den Spalten sollten zu diesem Zweck stets gleichgestaltet sein, also 1,00; 1,20; 1,23 und nicht 1; 1,2; 1,23.

## data2table_gh(data)

Die Funktion data2table_gh(string) kann Daten in eine Tabelle für das Github-eigene Markdown übersetzen und dabei eine wohlgeformte Tabelle erzeugen. Der Quellcode der Funktion ist noch Alpha, aber funktionstüchtig.

```python
data = """Jahr;DM;M;Wechselkurs;Kommentar
1970;1;1,80;1 : 1,8;
1975;1;2,20;1 : 2,2;
1980;1;2,50;1 : 2,5;
1987;1;4,00;1 : 4,0;
1988;1;4,40;1 : 4,4;
1989;1;5,00;1 : 5,0;Jahr der Wende"""

data2table_gh(data)
```

Ergibt dann fertig in einer Github-eigenen Readme-Datei z. B.:

| Jahr | DM |    M | Wechselkurs | Kommentar      | 
|:----:|:--:|-----:|:-----------:|:---------------|
| 1970 |  1 | 1,80 |     1 : 1,8 |                | 
| 1975 |  1 | 2,20 |     1 : 2,2 |                | 
| 1980 |  1 | 2,50 |     1 : 2,5 |                | 
| 1987 |  1 | 4,00 |     1 : 4,0 |                | 
| 1988 |  1 | 4,40 |     1 : 4,4 |                | 
| 1989 |  1 | 5,00 |     1 : 5,0 | Jahr der Wende | 

Anzumerken ist, dass an der fertigen Tabelle im Quelltext Korrekturen bei der Ausrichtung vorgenommen werden können, so unterstützt die Funktion z. B. keine Zentrierung. Rechtsbündig ist im Markdown "--:", linksbündig ist ":--" und zentriert wird in Zeile 2 mittels ":--:" eingestellt.
