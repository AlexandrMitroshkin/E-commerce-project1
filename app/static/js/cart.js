
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.quantity-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const itemId = this.closest('.cart-item').dataset.itemId;
            const action = this.dataset.action;
            
            fetch(`/update-cart/${itemId}`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ action: action })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const item = document.querySelector(`[data-item-id="${itemId}"]`);
                    
                    if (action === 'remove') {
                        item.remove();
                    } else {
                        item.querySelector('.quantity-value').textContent = data.quantity;
                        
                        const price = parseFloat(item.querySelector('.price').textContent.replace('$', ''));
                        item.querySelector('.item-total').textContent = '$' + (price * data.quantity).toFixed(2);
                    }
                    
                    document.getElementById('subtotal').textContent = '$' + data.subtotal.toFixed(2);
                    document.getElementById('delivery').textContent = '$' + data.delivery.toFixed(2);
                    document.getElementById('total').textContent = '$' + data.total.toFixed(2);
                    
                    if (!document.querySelector('.cart-item')) {
                        showEmptyCart();
                    }
                }
            });
        });
    });
    
    document.querySelectorAll('.remove-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const itemId = this.closest('.cart-item').dataset.itemId;
            
            if (confirm('Remove item?')) {
                fetch(`/update-cart/${itemId}`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ action: 'remove' })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        document.querySelector(`[data-item-id="${itemId}"]`).remove();
                        
                        document.getElementById('subtotal').textContent = '$' + data.subtotal.toFixed(2);
                        document.getElementById('delivery').textContent = '$' + data.delivery.toFixed(2);
                        document.getElementById('total').textContent = '$' + data.total.toFixed(2);
                        
                        if (!document.querySelector('.cart-item')) {
                            showEmptyCart();
                        }
                    }
                });
            }
        });
    });
});

function showEmptyCart() {
    document.querySelector('.cart-items').innerHTML = `
        <div class="empty-cart">
            <h3 style="margin-bottom: 10px;">Your cart is empty</h3>
            <p style="margin-bottom: 20px; color: #666;">Add some products to your cart</p>
            <a href="/" style="display: inline-block; padding: 12px 24px; background: black; color: white; border-radius: 30px; text-decoration: none;">
                Continue Shopping
            </a>
        </div>
    `;
}