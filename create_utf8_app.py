print("🚀 Создаем application.py в UTF-8 кодировке...")


app_content = '''from app import create_app

# Create Flask application
app = create_app()

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
'''


with open('application.py', 'w', encoding='utf-8') as f:
    f.write(app_content)

print("✅ application.py создан в UTF-8!")
print("\nСодержимое:")
print("-" * 30)
print(app_content)
print("-" * 30)