====================================================================================================
CÁLCULOS SOLARES - LONGYEARBYEN, SVALBARD (78.22°N, 15.63°E)
Equações NOAA - Dia 21 de cada mês de 2025 - Horário Local: UTC+1
====================================================================================================

      Mês        Data       Declinação (°)  EqTime (min)  cos(ha)  Nascer do Sol (UTC)  Pôr do Sol (UTC)  Fotoperíodo (h)  Meio-dia Solar (UTC)  Fenômeno
   January    21/01/2025            -19.95         -9.87    2.459                 N/A                 N/A              0.0                11.16h  Noite Polar
  February    21/02/2025            -10.37        -13.51    1.279                 N/A                 N/A              0.0                11.22h  Noite Polar
     March    21/03/2025              0.28         -7.24   -0.036              05.30h              17.40h             12.2                11.11h  Dia Normal
     April    21/04/2025             11.48          0.61   -0.436              00.54h              17.52h             17.0                10.98h  Dia Normal
       May    21/05/2025             20.15          3.38   -0.764                 N/A                 N/A             24.0                10.89h  Sol da Meia-Noite
      June    21/06/2025             23.44         -1.49   -2.042                 N/A                 N/A             24.0                10.99h  Sol da Meia-Noite
      July    21/07/2025             20.44         -6.18   -0.775                 N/A                 N/A             24.0                11.10h  Sol da Meia-Noite
    August    21/08/2025             12.32         -3.11   -0.467              00.47h              19.13h             18.4                10.99h  Dia Normal
 September    21/09/2025              1.09          7.52   -0.102              05.20h              18.06h             12.8                10.87h  Dia Normal
   October    21/10/2025            -10.44         15.39    1.288                 N/A                 N/A              0.0                10.74h  Noite Polar
  November    21/11/2025            -19.76         16.27    2.434                 N/A                 N/A              0.0                10.72h  Noite Polar
  December    21/12/2025            -23.44          1.96    2.042                 N/A                 N/A              0.0                10.87h  Noite Polar

================================================================================
ANÁLISE DOS RESULTADOS:
================================================================================
1. Meses com NOITE POLAR (Fotoperíodo = 0h):
   January, February, October, November, December

2. Meses com SOL DA MEIA-NOITE (Fotoperíodo = 24h):
   May, June, July

3. Meses com DIA/NORMAL (com nascer e pôr do sol):
   March, April, August, September

4. Valores extremos de cos(ha):
   Máximo (Noite Polar): 2.459 (janeiro)
   Mínimo (Sol Meia-Noite): -2.042 (junho)

5. Variação da declinação solar:
   Máxima: +23.44° (junho - solstício de verão)
   Mínima: -23.44° (dezembro - solstício de inverno)

6. Resumo do Fotoperíodo Anual:
   --------------------------------------------------
   January     |   0.0h | Noite Polar
   February    |   0.0h | Noite Polar
   March       |  12.2h | Dia Normal
   April       |  17.0h | Dia Normal
   May         |  24.0h | Sol da Meia-Noite
   June        |  24.0h | Sol da Meia-Noite
   July        |  24.0h | Sol da Meia-Noite
   August      |  18.4h | Dia Normal
   September   |  12.8h | Dia Normal
   October     |   0.0h | Noite Polar
   November    |   0.0h | Noite Polar
   December    |   0.0h | Noite Polar

================================================================================
VERIFICAÇÃO DOS CASOS POLARES (|cos(ha)| > 1):
================================================================================
January: cos(ha) = 2.459 → NOITE POLAR
   Declinação: -19.95°, tan(lat) = 4.707, tan(decl) = -0.363
   -tan(lat)*tan(decl) = 1.708

February: cos(ha) = 1.279 → NOITE POLAR
   Declinação: -10.37°, tan(lat) = 4.707, tan(decl) = -0.183
   -tan(lat)*tan(decl) = 0.861

May: cos(ha) = -0.764 → DIA NORMAL (mas NOAA considera > -1)
   Declinação: 20.15°, tan(lat) = 4.707, tan(decl) = 0.367
   -tan(lat)*tan(decl) = -1.728

June: cos(ha) = -2.042 → SOL DA MEIA-NOITE
   Declinação: 23.44°, tan(lat) = 4.707, tan(decl) = 0.434
   -tan(lat)*tan(decl) = -2.042

July: cos(ha) = -0.775 → DIA NORMAL (mas NOAA considera > -1)
   Declinação: 20.44°, tan(lat) = 4.707, tan(decl) = 0.373
   -tan(lat)*tan(decl) = -1.756

October: cos(ha) = 1.288 → NOITE POLAR
   Declinação: -10.44°, tan(lat) = 4.707, tan(decl) = -0.184
   -tan(lat)*tan(decl) = 0.867

November: cos(ha) = 2.434 → NOITE POLAR
   Declinação: -19.76°, tan(lat) = 4.707, tan(decl) = -0.359
   -tan(lat)*tan(decl) = 1.690

December: cos(ha) = 2.042 → NOITE POLAR
   Declinação: -23.44°, tan(lat) = 4.707, tan(decl) = -0.434
   -tan(lat)*tan(decl) = 2.042

================================================================================
RESULTADOS EXPORTADOS PARA: solar_calculations_longyearbyen_2025_noaa.csv
================================================================================

DATAFRAME COMPLETO (pandas):
        Mês        Data  Declinação (°)  EqTime (min)  cos(ha) Nascer do Sol (UTC) Pôr do Sol (UTC)  Fotoperíodo (h) Meio-dia Solar (UTC)          Fenômeno
0   January  21/01/2025          -19.95         -9.87    2.459                N/A                N/A              0.0               11.16h      Noite Polar
1  February  21/02/2025          -10.37        -13.51    1.279                N/A                N/A              0.0               11.22h      Noite Polar
2     March  21/03/2025            0.28         -7.24   -0.036             05.30h             17.40h             12.2               11.11h       Dia Normal
3     April  21/04/2025           11.48          0.61   -0.436             00.54h             17.52h             17.0               10.98h       Dia Normal
4       May  21/05/2025           20.15          3.38   -0.764                N/A                N/A             24.0               10.89h  Sol da Meia-Noite
5      June  21/06/2025           23.44         -1.49   -2.042                N/A                N/A             24.0               10.99h  Sol da Meia-Noite
6      July  21/07/2025           20.44         -6.18   -0.775                N/A                N/A             24.0               11.10h  Sol da Meia-Noite
7    August  21/08/2025           12.32         -3.11   -0.467             00.47h             19.13h             18.4               10.99h       Dia Normal
8  September  21/09/2025            1.09          7.52   -0.102             05.20h             18.06h             12.8               10.87h       Dia Normal
9   October  21/10/2025          -10.44         15.39    1.288                N/A                N/A              0.0               10.74h      Noite Polar
10  November  21/11/2025          -19.76         16.27    2.434                N/A                N/A              0.0               10.72h      Noite Polar
11  December  21/12/2025          -23.44          1.96    2.042                N/A                N/A              0.0               10.87h      Noite Polar
