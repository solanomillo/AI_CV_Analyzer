// JavaScript específico para result.html
    document.addEventListener('DOMContentLoaded', function() {
        console.log('Result page JavaScript cargado');
        
        // Efecto de scroll suave para elementos
        const resultCards = document.querySelectorAll('.result-card');
        
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
        
        resultCards.forEach(card => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            card.style.transition = 'all 0.6s ease';
            observer.observe(card);
        });
        
        // Copiar resumen al portapapeles (opcional)
        const summaryBox = document.querySelector('.summary-box');
        if (summaryBox) {
            summaryBox.style.cursor = 'pointer';
            summaryBox.title = 'Haz clic para copiar el resumen';
            
            summaryBox.addEventListener('click', function() {
                const textToCopy = this.textContent;
                navigator.clipboard.writeText(textToCopy).then(() => {
                    const originalContent = this.innerHTML;
                    this.innerHTML = '<div class="text-success"><i class="bi bi-check-circle-fill me-2"></i>¡Copiado al portapapeles!</div>';
                    
                    setTimeout(() => {
                        this.innerHTML = originalContent;
                    }, 2000);
                });
            });
        }
    });