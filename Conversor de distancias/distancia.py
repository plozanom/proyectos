# Sistema Internacional
def Km_a_m(km):
    return km * 1000

def Hm_a_m(hm):
    return hm * 100

def Dm_a_m(dm):
    return dm * 10

def dm_a_m(dm):
    return dm * 0.1

def cm_a_m(cm):
    return cm * 0.01

def mm_a_m(mm):
    return mm * 0.001

def um_a_m(um):
    return um / 1000000

def nm_a_m(nm):
    return nm / 1000000000

# Sistema Inglés o Imperial
def in_a_ft(pulg):
    return  pulg / 12

def ft_a_yd(ft):
    return ft / 3

def yd_a_mi(yd):
    return yd / 1760

def nmi_a_ft(nmi):
    return nmi * 6076.12

# Conversion entre sistemas
def in_a_cm(pulg):
    return pulg * 2.54

def cm_a_in(cm):
    return cm * 0.393701

def in_a_m(pulg):
    return pulg * 0.0254

def m_a_in(m):
    return m * 39.3701

def ft_a_m(ft):
    return ft * 0.3048

def m_a_ft(m):
    return m * 3.28084

def mi_a_km(mi):
    return mi * 1.60934

def km_a_mi(km):
    return km * 0.621371

def nmi_a_km(nmi):
    return nmi * 1.852

def km_a_nmi(km):
    return km / 1.852