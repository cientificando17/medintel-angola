from app import create_app
from app.extensions.db import db
from app.models.user import User
from datetime import datetime

def add_director_admin():
    """Adicionar Diretor Geral como Administrador"""
    
    app = create_app()
    
    with app.app_context():
        # Verificar se já existe
        existing = User.query.filter_by(email="botelholupapa@gmail.com").first()
        
        if existing:
            print(f"⚠️ Utilizador já existe!")
            print(f"   Nome: {existing.name}")
            print(f"   Email: {existing.email}")
            print(f"   Role: {existing.role}")
            print(f"   Verificado: {existing.is_verified}")
            
            # Atualizar para admin se não for
            if existing.role != 'admin':
                existing.role = 'admin'
                existing.is_verified = True
                existing.is_active = True
                existing.verification_status = 'approved'
                db.session.commit()
                print(f"✅ Utilizador atualizado para ADMIN!")
            return
        
        # Criar novo Administrador
        admin = User(
            name="Botelho Castro Lupapa",
            email="botelholupapa@gmail.com",
            role="admin",
            is_verified=True,
            is_active=True,
            verification_status='approved',
            specialty="Direção Geral",
            hospital="MedIntel Angola",
            registration_date=datetime.now()
        )
        admin.set_password("C4str0Lup4p4")  # Definir password
        
        db.session.add(admin)
        db.session.commit()
        
        print("=" * 50)
        print("✅ ADMINISTRADOR CRIADO COM SUCESSO!")
        print("=" * 50)
        print(f"📧 Email: botelholupapa@gmail.com")
        print(f"🔑 Password: C4str0Lup4p4")
        print(f"👤 Nome: Botelho Castro Lupapa")
        print(f"⭐ Role: Administrador")
        print("=" * 50)

if __name__ == "__main__":
    add_director_admin()