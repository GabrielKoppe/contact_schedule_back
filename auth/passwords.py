import bcrypt

def cod_senha(senha_entrada):
    return bcrypt.hashpw(senha_entrada.encode('utf8'), bcrypt.gensalt())

def compara_senha(senha_banco, senha_entrada):
    return bcrypt.checkpw(senha_entrada.encode('utf8'), senha_banco.encode('utf8'))