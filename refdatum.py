# This is reference data for use by the Datum module.
#
# First we'll define some standard ellipsoids
# then we'll use those to define standard datums
#
# The following data are culled from Peter Dana's excellent sites at
# http://www.colorado.edu/geography/gcraft/notes/datum/datum.html and
# http://www.ncgia.ucsb.edu/education/curricula/giscc/units/u015/u015.html
# Gosh, was that fun!
#
#


Ellipsoids = {
    "Airy 1830":                ( 6377563.396, 299.3249646),
    "Modified Airy":            ( 6377340.189, 299.3249646),
    "Australian National":      ( 6378160,     298.25),
    "Bessel 1841 (Namibia)":    ( 6377483.865, 299.1528128),
    "Bessel 1841":              ( 6377397.155, 299.1528128),
    "Clarke 1866":              ( 6378206.4,   294.9786982),
    "Clarke 1880":              ( 6378249.145, 293.465),
    "Everest (India 1830)":     ( 6377276.345, 300.8017),
    "Everest (Sabah Sarawak)":  ( 6377298.556, 300.8017),
    "Everest (India 1956)":     ( 6377301.243, 300.8017),
    "Everest (Malaysia 1969)":  ( 6377295.664, 300.8017),
    "Everest (Malay. & Sing)":  ( 6377304.063, 300.8017),
    "Everest (Pakistan)":       ( 6377309.613, 300.8017),
    "Modified Fischer 1960":    ( 6378155,     298.3),
    "Helmert 1906":             ( 6378200,     298.3),
    "Hough 1960":               ( 6378270,     297),
    "Indonesian 1974":          ( 6378160,     298.247),
    "International 1924":       ( 6378388,     297),
    "Krassovsky 1940":          ( 6378245,     298.3),
    "GRS 80":                   ( 6378137,     298.257222101),
    "South American 1969":      ( 6378160,     298.25),
    "WGS 72":                   ( 6378135,     298.26),
    "WGS 84":                   ( 6378137,     298.257223563),
}


Datums = {
'Adindan':                     ('Clarke 1880'            , -166,  -15,  204),
'Afgooye':                     ('Krassovsky 1940'        ,  -43, -163,   45),
'Ain El Abd 1970':             ('International 1924'     , -150, -251,   -2),
'Alaska (NAD-27)':             ('Clarke 1866'            ,   -5,  135,  172),
'Alaska/Canada NAD-27':        ('Clarke 1866'            ,   -9,  151,  185),
'Anna 1 Astro 1965':           ('Australian National'    , -491,  -22,  435),
'ARC-1950 mean':               ('Clarke 1880'            , -143,  -90, -294),
'ARC-1960 mean':               ('Clarke 1880'            , -160,   -8, -300),
'Ascension Island 58':         ('International 1924'     , -207,  107,   52),
'Astro B4 Sor.Atoll':          ('International 1924'     ,  114, -116, -333),
'Astro Beacon E':              ('International 1924'     ,  145,   75, -272),
'Astro Pos 71/4':              ('International 1924'     , -320,  550, -494),
'Astronomic Stn. 52':          ('International 1924'     ,  124, -234,  -25),
'Australian Geodetic 1984':    ('Australian National'    , -134,  -48,  149),
'Bahamas (NAD-27)':            ('Clarke 1866'            ,   -4,  154,  178),
'Bellevue (IGN)':              ('International 1924'     , -127, -769,  472),
'Bermuda 1957':                ('Clarke 1866'            ,  -73,  213,  296),
'Bogota Observatory':          ('International 1924'     ,  307,  304, -318),
'Bukit Rimpah':                ('Bessel 1841'            , -384,  664,  -48),
'Camp Area Astro':             ('International 1924'     , -104, -129,  239),
'Campo Inchauspe':             ('International 1924'     , -148,  136,   90),
'Canada Mean (NAD27)':         ('Clarke 1866'            ,  -10,  158,  187),
'Canal Zone (NAD27)':          ('Clarke 1866'            ,    0,  125,  201),
'Canton Island 1966':          ('International 1924'     ,  298, -304, -375),
'Cape':                        ('Clarke 1880'            , -136, -108, -292),
'Cape Canaveral mean':         ('Clarke 1866'            ,   -2,  150,  181),
'Carribean (NAD27)':           ('Clarke 1866'            ,   -7,  152,  178),
'Carthage':                    ('Clarke 1880'            , -263,    6,  431),
'Central America (NAD27)':     ('Clarke 1866'            ,    0,  125,  194),
'Chatham 1971':                ('International 1924'     ,  175,  -38,  113),
'Chua Astro':                  ('International 1924'     , -134,  229,  -29),
'Corrego Alegre':              ('International 1924'     , -206,  172,   -6),
'Corrego Alegre (Provisional)': ('International 1924'    , -206,  172,   -6),
'Cuba (NAD27)':                ('Clarke 1866'            ,   -9,  152,  178),
'Cyprus':                      ('International 1924'     , -104, -101, -140),
'Djakarta(Batavia)':           ('Bessel 1841'            , -377,  681,  -50),
'DOS 1968':                    ('International 1924'     ,  230, -199, -752),
'Easter lsland 1967':          ('International 1924'     ,  211,  147,  111),
'Egypt':                       ('International 1924'     , -130, -117, -151),
'European 1950':               ('International 1924'     ,  -87,  -96, -120),
'European 1950 mean':          ('International 1924'     ,  -87,  -98, -121),
'European 1979 mean':          ('International 1924'     ,  -86,  -98, -119),
'Finnish Nautical Chart':      ('International 1924'     ,  -78, -231,  -97),
'Gandajika Base':              ('International 1924'     , -133, -321,   50),
'Geodetic Datum 49':           ('International 1924'     ,   84,  -22,  209),
'Ghana':                       ('WGS 84'                 ,    0,    0,    0),
'Greenland (NAD27)':           ('Clarke 1866'            ,   11,  114,  195),
'Guam 1963':                   ('Clarke 1866'            , -100, -248,  259),
'Gunung Segara':               ('Bessel 1841'            , -403,  684,   41),
'Gunung Serindung 1962':       ('WGS 84'                 ,    0,    0,    0),
'GUX 1 Astro':                 ('International 1924'     ,  252, -209, -751),
'Herat North':                 ('International 1924'     , -333, -222,  114),
'Hjorsey 1955':                ('International 1924'     ,  -73,   46,  -86),
'Hong Kong 1963':              ('International 1924'     , -156, -271, -189),
'Hu-Tzu-Shan':                 ('International 1924'     , -634, -549, -201),
'Indian':                      ('Everest (India 1830)'   ,  289,  734,  257),
'Iran':                        ('International 1924'     , -117, -132, -164),
'Ireland 1965':                ('Modified Airy'          ,  506, -122,  611),
'ISTS 073 Astro 69':           ('International 1924'     ,  208, -435, -229),
'Johnston Island 61':          ('International 1924'     ,  191,  -77, -204),
'Kandawala':                   ('Everest (India 1830)'   ,  -97,  787,   86),
'Kerguelen Island':            ('International 1924'     ,  145, -187,  103),
'Kertau 48':                   ('Everest (Malay. & Sing)',  -11,  851,    5),
'L.C. 5 Astro':                ('Clarke 1866'            ,   42,  124,  147),
'La Reunion':                  ('International 1924'     ,   94, -948, -1262),
'Liberia 1964':                ('Clarke 1880'            ,  -90,   40,   88),
'Luzon':                       ('Clarke 1866'            , -133,  -77,  -51),
'Mahe 1971':                   ('Clarke 1880'            ,   41, -220, -134),
'Marco Astro':                 ('International 1924'     , -289, -124,   60),
'Masirah Is. (Nahrwan)':       ('Clarke 1880'            , -247, -148,  369),
'Massawa':                     ('Bessel 1841'            ,  639,  405,   60),
'Merchich':                    ('Clarke 1880'            ,   31,  146,   47),
'Mexico (NAD27)':              ('Clarke 1866'            ,  -12,  130,  190),
'Midway Astro 61':             ('International 1924'     ,  912,  -58, 1227),
'Mindanao':                    ('Clarke 1866'            , -133,  -79,  -72),
'Minna':                       ('Clarke 1880'            ,  -92,  -93,  122),
'Montjong Lowe':               ('WGS 84'                 ,    0,    0,    0),
'Nahrwan':                     ('Clarke 1880'            , -231, -196,  482),
'Naparima BWI':                ('International 1924'     ,   -2,  374,  172),
'North America 83':            ('GRS 80'                 ,    0,    0,    0),
'North America 1927 mean':     ('Clarke 1866'            ,   -8,  160,  176),
'Observatorio 1966':           ('International 1924'     , -425, -169,   81),
'Old Egyptian':                ('Helmert 1906'           , -130,  110,  -13),
'Old Hawaiian mean':           ('Clarke 1866'            ,   89, -279, -183),
'Old Hawaiian Kauai':          ('Clarke 1866'            ,   45, -290, -172),
'Old Hawaiian Maui':           ('Clarke 1866'            ,   65, -290, -190),
'Old Hawaiian Oahu':           ('Clarke 1866'            ,   56, -284, -181),
'Oman':                        ('Clarke 1880'            , -346,   -1,  224),
'Ordnance Survey of Great Britain 36': ('Airy 1830'      ,  375, -111,  431),
'Pico De Las Nieves':          ('International 1924'     , -307,  -92,  127),
'Pitcairn Astro 67':           ('International 1924'     ,  185,  165,   42),
'Potsdam Rauenberg DHDN':      ('Bessel 1841'            ,  606,   23,  413),
'Provisional South American 1956 mean':
                               ('International 1924'     , -288,  175, -376),
'Provisional South Chilean 1963': ('International 1924'  ,   16,  196,   93),
'Puerto Rico':                 ('Clarke 1866'            ,   11,   72, -101),
'Pulkovo 1942':                ('Krassovsky 1940'        ,   28, -130,  -95),
'Qornoq':                      ('International 1924'     ,  164,  138, -189),
'Quatar National':             ('International 1924'     , -128, -283,   22),
'Rome 1940':                   ('International 1924'     , -225,  -65,    9),
'S 42':                        ('Krassovsky 1940'        ,   28, -121,  -77),
'S.E.Asia (Indian)':           ('Everest (India 1830)'   ,  173,  750,  264),
'SAD-69/Brazil':               ('South American 1969'    ,  -60,   -2,  -41),
'Santa Braz':                  ('International 1924'     , -203,  141,   53),
'Santo (DOS)':                 ('International 1924'     ,  170,   42,   84),
'Sapper Hill 43':              ('International 1924'     , -355,   16,   74),
'Schwarzeck':                  ('Bessel 1841 (Namibia)'  ,  616,   97, -251),
'Sicily':                      ('International 1924'     ,  -97,  -88, -135),
'Sierra Leone 1960':           ('WGS 84'                 ,    0,    0,    0),
'South American 1969 mean':    ('South American 1969'    ,  -57,    1,  -41),
'South American 1969 mean':    ('South American 1969'    ,  -57,    1,  -41),
'South Asia':                  ('Modified Fischer 1960'  ,    7,  -10,  -26),
'Southeast Base':              ('International 1924'     , -499, -249,  314),
'Southwest Base':              ('International 1924'     , -104,  167,  -38),
'Tananarive Observatory 25':   ('International 1924'     , -189, -242,  -91),
'Thai/Viet (Indian)':          ('Everest (India 1830)'   ,  214,  836,  303),
'Timbalai 1948':               ('Everest (India 1830)'   , -689,  691,  -45),
'Tokyo mean':                  ('Bessel 1841'            , -128,  481,  664),
'Tristan Astro 1968':          ('International 1924'     , -632,  438, -609),
'Unites Arab Emirates (Nahrwan)': ('Clarke 1880'         , -249, -156,  381),
'Viti Levu 1916':              ('Clarke 1880'            ,   51,  391,  -36),
'Wake-Eniwetok 60':            ('Hough 1960'             ,  101,   52,  -39),
'WGS 72':                      ('WGS 72'                 ,    0,    0,    5),
'WGS 84':                      ('WGS 84'                 ,    0,    0,    0),
'Yacare':                      ('International 1924'     , -155,  171,   37),
'Zanderij':                    ('International 1924'     , -265,  120, -358),

}

# ----------------------------
