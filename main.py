print('\n')

monto_total_pc, paga_total_pc = 0, 0

def pp_a_pc(pp: int):
    pc = pp*10
    return pc

def po_a_pc(pp: int):
    pc = pp*100
    return pc

def ppt_a_pc(pp: int):
    pc = pp*1000
    return pc

def monto_a_pc(pc:int, pp:int, po:int, ppt:int):
    pp = pp_a_pc(pp)
    po = po_a_pc(po)
    ppt = ppt_a_pc(ppt)
    total = pc + pp + po + ppt
    return total


def pc_a_pp(pc: int):
    pp = pc//10
    pc = pc%10
    return pp, pc

def pc_a_po(pc: int):
    po = pc//100
    pc = pc%100
    return po, pc

def pc_a_ppt(pc: int):
    ppt = pc//1000
    pc = pc%1000
    return ppt, pc

def calcular_vuelto(pc: int):
    ppt, pc = pc_a_ppt(pc)
    po, pc = pc_a_po(pc)
    pp, pc = pc_a_pp(pc)
    return pc, pp, po, ppt



# Monto a pagar
def preguntar_monto():
    global monto_total_pc
    print('--- PRECIO A PAGAR ---')
    monto_pc = int(input('Piezas de cobre a pagar: '))
    monto_pp = int(input('Piezas de plata a pagar: '))
    monto_po = int(input('Piezas de oro a pagar: '))
    monto_ppt = int(input('Piezas de platino a pagar: '))

    monto_total_pc = monto_a_pc(monto_pc, monto_pp, monto_po, monto_ppt)

    print('\nTotal a pagar en PC: ', monto_total_pc)
    print('\n')


# Paga con
def preguntar_paga():
    global paga_total_pc
    print('--- PAGA CON ---')
    paga_pc = int(input('Piezas de cobre con que paga: '))
    paga_pp = int(input('Piezas de plata con que paga: '))
    paga_po = int(input('Piezas de oro con que paga: '))
    paga_ppt = int(input('Piezas de platino con que paga: '))

    paga_total_pc = monto_a_pc(paga_pc, paga_pp, paga_po, paga_ppt)

    print('\nTotal en PC', paga_total_pc)
    print('\n')


# Calcular diferencia
def resultado():
    global paga_total_pc
    global monto_total_pc

    diferencia = paga_total_pc - monto_total_pc

    # Convertir vuelto a monedas
    pc, pp, po, ppt = calcular_vuelto(diferencia)
    print('--- VUELTO ---')
    vuelto = f"PC: {pc}\nPP: {pp}\nPO: {po}\nPPT: {ppt}"
    print(vuelto)

if __name__ == "__main__":
    preguntar_monto()
    preguntar_paga()
    resultado()