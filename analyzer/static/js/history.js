// JavaScript específico para history.html
    document.addEventListener('DOMContentLoaded', function() {
        console.log('History page JavaScript cargado');
        
        // Variables para el modal de eliminación
        const deleteModal = document.getElementById('deleteModal');
        const modalPosition = document.getElementById('modalPosition');
        let deleteUrl = '';
        
        // Manejar clic en botones de eliminar
        document.querySelectorAll('.history-action-btn.delete').forEach(button => {
            button.addEventListener('click', function() {
                const analysisId = this.getAttribute('data-analysis-id');
                const position = this.getAttribute('data-analysis-position');
                
                modalPosition.textContent = position;
                deleteUrl = "{% url 'delete_analysis' 0 %}".replace('0', analysisId);
                
                // Mostrar modal
                deleteModal.style.display = 'flex';
            });
        });
        
        // Manejar botones del modal
        document.getElementById('cancelDelete').addEventListener('click', function() {
            deleteModal.style.display = 'none';
            deleteUrl = '';
        });
        
        document.getElementById('confirmDelete').addEventListener('click', function() {
            if (deleteUrl) {
                window.location.href = deleteUrl;
            }
        });
        
        // Cerrar modal al hacer clic fuera
        deleteModal.addEventListener('click', function(e) {
            if (e.target === deleteModal) {
                deleteModal.style.display = 'none';
                deleteUrl = '';
            }
        });
        
        // Funcionalidad de búsqueda
        const searchInput = document.getElementById('historySearch');
        const historyItems = document.querySelectorAll('.history-analysis-item');
        
        if (searchInput) {
            searchInput.addEventListener('input', function() {
                const searchTerm = this.value.toLowerCase();
                
                historyItems.forEach(item => {
                    const text = item.textContent.toLowerCase();
                    if (text.includes(searchTerm)) {
                        item.style.display = 'block';
                        item.style.animation = 'history-slideIn 0.3s ease-out';
                    } else {
                        item.style.display = 'none';
                    }
                });
            });
        }
        
        // Funcionalidad de filtrado por fecha
        const dateFilter = document.getElementById('historyDateFilter');
        if (dateFilter) {
            dateFilter.addEventListener('change', function() {
                // Esta función se implementaría con AJAX o recargando la página
                console.log('Filtrar por fecha:', this.value);
                // window.location.href = `?date_filter=${this.value}`;
            });
        }
        
        // Funcionalidad de ordenamiento
        const sortSelect = document.getElementById('historySort');
        if (sortSelect) {
            sortSelect.addEventListener('change', function() {
                // Esta función se implementaría con AJAX o recargando la página
                console.log('Ordenar por:', this.value);
                // window.location.href = `?sort=${this.value}`;
            });
        }
        
        // Animación al hacer scroll
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, {
            threshold: 0.1
        });
        
        historyItems.forEach(item => {
            item.style.opacity = '0';
            item.style.transform = 'translateY(20px)';
            item.style.transition = 'all 0.6s ease';
            observer.observe(item);
        });
    });