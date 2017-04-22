

def convert_basis_function(in_str):
    # possible values: 'CONSENT SEARCH', 'REASONABLE SUSPICION', nan, 'PROBABLE CAUSE'
    if in_str == 'CONSENT SEARCH':
        out_str = 'Consented to be Search'
    elif in_str == 'REASONABLE SUSPICION':
        out_str = 'Reasonable Suspicion'
    elif in_str == 'PROBABLE CAUSE':
        out_str = 'Probable Cause'
    else:
        out_str = 'delete'

    return out_str


def convert_race_function(in_str):
    ''' possible values: 'B(Black)', 'W(White)', 'NO DATA ENTERED', 'UNKNOWN', 'H(Hispanic)',
       'I(American Indian or Alaskan Native)',
       'A(Asian or Pacific Islander)', 'M(Middle Eastern or East Indian)' '''

    if in_str == 'B(Black)':
        out_str = 'black'
    elif in_str == 'W(White)':
        out_str = 'white'
    elif in_str == 'H(Hispanic)':
        out_str = 'hispanic'
    elif in_str == 'I(American Indian or Alaskan Native)':
        out_str = 'american indian'
    elif in_str == 'A(Asian or Pacific Islander)':
        out_str = 'asian'
    elif in_str == 'M(Middle Eastern or East Indian)':
        out_str = 'middle eastern'
    else:
        out_str = 'delete'

    return out_str


def convert_fiofs_type_function(in_str):
    ''' possible values: 'IOFS', 'IO', 'IOF', 'OF', 'I', 'O', 'IF', 'IFS', 'F', 'OFS', 'IS',
       'IOS', 'OS', 'S', 'FS', 'PI', 'PIO', 'PIOS', 'PO', 'PIOFS', 'PIF',
       'PIOF', 'P', 'PIS', 'PF', 'POF' '''

    if in_str == 'O':
        out_str = 'observed'
    elif (in_str == 'IOFS' or in_str == 'IO' or in_str == 'IOF' or in_str == 'OF' or in_str == 'I' or in_str == 'IF' or \
         in_str == 'IFS' or in_str == 'F' or in_str == 'OFS' or in_str == 'IS' or in_str == 'IOS' or in_str == 'OS' or \
         in_str == 'S' or in_str == 'FS'):
        out_str = 'stopped'
    else:
        out_str = 'delete'

    return out_str