# 🚀 DEPLOY MANUAL RAILWAY - SISTEMA JAM

## ✅ **DEPLOY GRATUITO PASSO A PASSO**

Siga estes passos para colocar o Sistema JAM online gratuitamente!

## 📋 **Passo 1: Login no Railway**

Abra o terminal e execute:
```bash
railway login
```

Isso abrirá seu navegador para fazer login no Railway.

## 📋 **Passo 2: Criar Projeto**

Execute:
```bash
railway init
```

Escolha:
- **Create new project** (Criar novo projeto)
- Nome: `sistema-jam`

## 📋 **Passo 3: Adicionar Banco de Dados**

No dashboard do Railway:
1. Clique em **"New"**
2. Selecione **"Database"**
3. Escolha **"PostgreSQL"**
4. Aguarde a criação

## 📋 **Passo 4: Configurar Variáveis de Ambiente**

No projeto Railway, vá em **"Variables"** e adicione:

```
DJANGO_SETTINGS_MODULE=empresa_nova.settings_railway
SECRET_KEY=sua-chave-secreta-aqui
DATABASE_URL=postgresql://...
```

## 📋 **Passo 5: Fazer Deploy**

Execute:
```bash
railway up
```

## 🌐 **URLs Finais**

Após o deploy, o sistema estará em:
- **Site**: https://sistema-jam-production.up.railway.app
- **ERP**: https://sistema-jam-production.up.railway.app/sistema/
- **Admin**: https://sistema-jam-production.up.railway.app/admin/

## 🔑 **Credenciais**
```
Usuário: admin
Senha: SistemaJam2024!
```

## 🎯 **Vantagens do Railway**

### ✅ **Gratuito**
- 500 horas/mês
- Banco PostgreSQL
- SSL automático
- Domínio personalizado

### ✅ **Profissional**
- 99.9% uptime
- Deploy automático
- Logs em tempo real
- Monitoramento

## 🚀 **Comandos Úteis**

```bash
# Status do projeto
railway status

# Ver logs
railway logs

# Reiniciar
railway restart

# Abrir no navegador
railway open
```

## 📞 **Suporte**

Se precisar de ajuda:
1. Dashboard: https://railway.app
2. Documentação: https://docs.railway.app
3. Comunidade: Discord Railway

## 🎉 **RESULTADO**

**O Sistema JAM estará online com:**
- ✅ Domínio profissional
- ✅ SSL/HTTPS
- ✅ Banco PostgreSQL
- ✅ Deploy automático
- ✅ Monitoramento 24/7

**O ERP mais moderno do mundo, gratuito!** 🚀

---

**Tempo estimado**: ⚡ **5 minutos**
**Custo**: 🆓 **GRATUITO**
**Status**: ✅ **PRONTO PARA DEPLOY**

**Execute os comandos acima e o Sistema JAM estará online!** 🎯 