#!/usr/bin/env python3
# ============================================================
#  servidor_rapido.py — Servidor HTTP OTIMIZADO
# ============================================================

import http.server
import socketserver
import os
from http.server import SimpleHTTPRequestHandler

PORT = 8000

# Mudar para pasta raiz
os.chdir('..')

class FastHTTPRequestHandler(SimpleHTTPRequestHandler):
    """Handler otimizado com cache e CORS"""
    
    # Desabilitar logs verbosos
    def log_message(self, format, *args):
        pass  # Silencioso = mais rápido
    
    def end_headers(self):
        # CORS
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        
        # CACHE para arquivos estáticos
        path = self.path.lower()
        if any(path.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.ico', '.woff', '.woff2', '.ttf']):
            # Cache de 1 hora para imagens e fontes
            self.send_header('Cache-Control', 'public, max-age=3600')
        elif any(path.endswith(ext) for ext in ['.css', '.js']):
            # Cache de 10 minutos para CSS/JS
            self.send_header('Cache-Control', 'public, max-age=600')
        else:
            # Sem cache para HTML e JSON
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        
        super().end_headers()

# Usar ThreadingHTTPServer para requisições paralelas
class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

print("=" * 60)
print("  SERVIDOR RÁPIDO PGV5")
print("=" * 60)
print(f"\n⚡ Modo: Multi-threaded (paralelo)")
print(f"🌐 URL: http://localhost:{PORT}")
print(f"📁 Pasta: {os.getcwd()}")
print("\n🔗 Acesse:")
print(f"   http://localhost:{PORT}/index.html")
print("\n💡 Dica: CTRL+C para parar")
print("\n" + "=" * 60 + "\n")

try:
    with ThreadingHTTPServer(("", PORT), FastHTTPRequestHandler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n\n✅ Servidor encerrado!")
except Exception as e:
    print(f"\n❌ Erro: {e}")
