from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Lógica para exibir produtos na página inicial
    return render_template('index.html')


@main.route('/product/<int:product_id>')
def product(product_id):
    # Lógica para exibir detalhes do produto
    return render_template('product.html', product_id=product_id)


admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def admin_dashboard():
    # Lógica para exibir o painel de administração
    return render_template('admin/dashboard.html')

@admin.route('/products')
def admin_products():
    # Lógica para exibir lista de produtos no painel de administração
    return render_template('admin/products.html')
