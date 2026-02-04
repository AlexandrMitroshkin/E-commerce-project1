
import os
import sys

print("🔍 Railway Database Checker")
print("=" * 60)

print("\n1. Checking directories:")
print(f"   Current dir: {os.getcwd()}")
print(f"   /tmp exists: {os.path.exists('/tmp')}")
print(f"   Can write to /tmp: {os.access('/tmp', os.W_OK)}")

print("\n2. Testing file creation:")
try:
    test_path = '/tmp/test_railway.txt'
    with open(test_path, 'w') as f:
        f.write('Railway test')
    print(f"   ✅ Created {test_path}")
    os.remove(test_path)
    print(f"   ✅ Removed {test_path}")
except Exception as e:
    print(f"   ❌ Failed: {e}")

print("\n3. Testing database:")
try:
    sys.path.insert(0, os.path.dirname(__file__))
    from app import create_app, db
    from app.models import Product
    
    app = create_app()
    
    with app.app_context():

        db.create_all()
        print("   ✅ Tables created")

        count = Product.query.count()
        print(f"   ✅ Products in DB: {count}")
        
except Exception as e:
    print(f"   ❌ Database error: {e}")

print("\n" + "=" * 60)
print("✅ Check completed")