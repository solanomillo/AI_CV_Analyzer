    // JavaScript específico para home.html
    document.addEventListener('DOMContentLoaded', function() {
        // Solo se ejecuta en home.html
        console.log('Home page JavaScript cargado');
        
        // Mejorar los labels del formulario
        const formLabels = document.querySelectorAll('.home-form-container label');
        formLabels.forEach(label => {
            label.classList.add('home-form-label');
        });

        // Agregar efecto al botón de submit
        const submitBtn = document.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.addEventListener('click', function() {
                this.innerHTML = '<i class="bi bi-hourglass-split me-2"></i> Procesando...';
                this.classList.add('disabled');
            });
        }

        // Validación simple de archivo
        const fileInput = document.querySelector('input[type="file"]');
        if (fileInput) {
            fileInput.addEventListener('change', function() {
                if (this.files.length > 0) {
                    const file = this.files[0];
                    const fileSize = file.size / 1024 / 1024; // MB
                    const allowedTypes = ['application/pdf', 'application/msword', 
                                         'application/vnd.openxmlformats-officedocument.wordprocessingml.document'];
                    
                    if (fileSize > 10) {
                        alert('El archivo es demasiado grande. El tamaño máximo es 10MB.');
                        this.value = '';
                    } else if (!allowedTypes.includes(file.type)) {
                        alert('Formato no soportado. Por favor, sube un PDF, DOC o DOCX.');
                        this.value = '';
                    }
                }
            });
        }
    });