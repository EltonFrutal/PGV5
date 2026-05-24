# ============================================================
#  pg_login.py — Página de Login (Consys - Sem Debug)
# ============================================================

def gerar():
    """Gera página de login sem debug"""
    
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PGV5 - Login</title>

<!-- Favicon e ícones -->
<link rel="icon" type="image/png" sizes="32x32" href="imagem/logos/sistema.png">
<link rel="icon" type="image/png" sizes="16x16" href="imagem/logos/sistema.png">
<link rel="apple-touch-icon" sizes="180x180" href="imagem/logos/sistema.png">
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#5B9FED">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="PGV5">

<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html, body {
  height: 100%;
  margin: 0;
}

body {
  font-family: 'Plus Jakarta Sans', sans-serif;
  background: linear-gradient(135deg, #5B9FED 0%, #4A90E2 50%, #3B7DD6 100%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.login-container {
  width: 100%;
  max-width: 420px;
}

.login-card {
  background: #fff;
  border-radius: 28px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
}

.login-header {
  background: linear-gradient(135deg, #5B9FED 0%, #4A90E2 100%);
  padding: 32px 32px 48px;
  text-align: center;
  position: relative;
}

.login-header::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 32px;
  background: #fff;
  border-radius: 28px 28px 0 0;
}

.logo-consys {
  width: 80px;
  height: 80px;
  margin: 0 auto 16px;
  position: relative;
  z-index: 1;
  background: rgba(255, 255, 255, 0.25);
  border-radius: 16px;
  padding: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo-consys img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
}

.consys-nome {
  font-size: 2rem;
  font-weight: 800;
  color: #fff;
  margin-bottom: 4px;
  position: relative;
  z-index: 1;
}

.consys-tagline {
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.9);
  font-weight: 500;
  position: relative;
  z-index: 1;
}

.login-body {
  padding: 28px 32px 32px;
}

.login-title {
  font-size: 1.6rem;
  font-weight: 700;
  color: #334155;
  text-align: center;
  margin-bottom: 28px;
}

.form-group {
  margin-bottom: 16px;
  position: relative;
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  background: #F8FAFC;
  border: 2px solid #E2E8F0;
  border-radius: 14px;
  padding: 14px 16px;
  transition: all 0.3s;
}

.input-wrapper:focus-within {
  background: #fff;
  border-color: #5B9FED;
  box-shadow: 0 0 0 3px rgba(91, 159, 237, 0.1);
}

.input-icon {
  width: 20px;
  height: 20px;
  margin-right: 12px;
  color: #5B9FED;
}

.form-input {
  flex: 1;
  border: none;
  background: transparent;
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 0.95rem;
  font-weight: 500;
  color: #334155;
  outline: none;
}

.form-input::placeholder {
  color: #94A3B8;
}

.btn-eye {
  background: transparent;
  border: none;
  padding: 4px;
  cursor: pointer;
  color: #94A3B8;
  transition: color 0.2s;
}

.btn-eye:hover {
  color: #5B9FED;
}

.btn-entrar {
  width: 100%;
  background: linear-gradient(135deg, #5B9FED 0%, #4A90E2 100%);
  border: none;
  border-radius: 14px;
  color: #fff;
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 1rem;
  font-weight: 700;
  padding: 15px;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 6px 20px rgba(91, 159, 237, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}

.btn-entrar:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 28px rgba(91, 159, 237, 0.4);
}

.btn-entrar:active {
  transform: translateY(0);
}

.arrow-icon {
  width: 20px;
  height: 20px;
}

.login-erro {
  background: #FEF2F2;
  border: 2px solid #FECACA;
  border-radius: 10px;
  color: #DC2626;
  font-size: 0.85rem;
  font-weight: 600;
  padding: 12px 16px;
  text-align: center;
  margin-bottom: 16px;
  display: none;
}

.login-footer {
  text-align: center;
  padding-top: 20px;
  border-top: 1px solid #F1F5F9;
  margin-top: 20px;
}

.footer-text {
  font-size: 0.75rem;
  color: #94A3B8;
  font-weight: 500;
  line-height: 1.5;
}

.footer-text .consys-link {
  color: #5B9FED;
  text-decoration: none;
  font-weight: 600;
}

@keyframes fadeUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.login-card {
  animation: fadeUp 0.6s ease both;
}

@media(max-width: 480px) {
  .login-header {
    padding: 28px 28px 44px;
  }
  
  .logo-consys {
    width: 70px;
    height: 70px;
  }
  
  .consys-nome {
    font-size: 1.75rem;
  }
  
  .login-body {
    padding: 24px 28px 28px;
  }
  
  .login-title {
    font-size: 1.4rem;
  }
}
</style>
</head>
<body>

<div class="login-container">
  <div class="login-card">
    <div class="login-header">
      <div class="logo-consys">
        <img src="imagem/logos/sistema.png" alt="Logo Consys">
      </div>
      <div class="consys-nome">Consys</div>
      <div class="consys-tagline">Consultoria e Sistemas</div>
    </div>
    
    <div class="login-body">
      <h1 class="login-title">Painel Gerencial</h1>
      
      <div class="login-erro" id="login-erro">
        E-mail ou senha incorretos
      </div>
      
      <form onsubmit="return false;">
        <div class="form-group">
          <div class="input-wrapper">
            <svg class="input-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
            <input 
              type="email" 
              class="form-input" 
              id="inp-email" 
              placeholder="Usuário" 
              autocomplete="username"
              onkeydown="if(event.key==='Enter')login()"
            >
          </div>
        </div>
        
        <div class="form-group">
          <div class="input-wrapper">
            <svg class="input-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
            </svg>
            <input 
              type="password" 
              class="form-input" 
              id="inp-senha" 
              placeholder="Senha" 
              autocomplete="current-password"
              onkeydown="if(event.key==='Enter')login()"
            >
            <button type="button" class="btn-eye" onclick="toggleSenha()">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                <circle cx="12" cy="12" r="3"></circle>
              </svg>
            </button>
          </div>
        </div>
        
        <button type="button" class="btn-entrar" onclick="login()">
          Entrar
          <svg class="arrow-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
          </svg>
        </button>
      </form>
      
      <div class="login-footer">
        <p class="footer-text">
          desenvolvido por<br>
          <a href="#" class="consys-link">Consys</a> Consultoria e Sistemas
        </p>
      </div>
    </div>
  </div>
</div>

<script>
var USUARIOS = [
  {id: 1, nome: 'elton@hotmail.com', senha: '123', perfil: 'Administrador', foto: 'imagem/fotos/elton@hotmail.com.jpg'},
  {id: 2, nome: 'afonso@hotmail.com', senha: '123', perfil: 'Consultor', foto: 'imagem/fotos/afonso@hotmail.com.jpg'}
];

function toggleSenha() {
  var inp = document.getElementById('inp-senha');
  inp.type = inp.type === 'password' ? 'text' : 'password';
}

function login() {
  var email = document.getElementById('inp-email').value.trim().toLowerCase();
  var senha = document.getElementById('inp-senha').value;
  var errorMsg = document.getElementById('login-erro');
  
  var user = USUARIOS.find(u => u.nome.toLowerCase() === email && u.senha === senha);
  
  if (user) {
    localStorage.setItem('pgv5_usuario_id', user.id);
    localStorage.setItem('pgv5_usuario_nome', user.nome);
    localStorage.setItem('pgv5_usuario_perfil', user.perfil);
    localStorage.setItem('pgv5_usuario_foto', user.foto);
    window.location.href = 'empresas.html';
  } else {
    errorMsg.style.display = 'block';
    setTimeout(() => {
      errorMsg.style.display = 'none';
    }, 3000);
  }
}

localStorage.removeItem('pgv5_usuario_id');
localStorage.removeItem('pgv5_empresa_id');
localStorage.removeItem('pgv5_usuario_foto');
</script>

</body>
</html>
"""
