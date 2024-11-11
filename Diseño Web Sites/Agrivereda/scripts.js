const cultivoInfoElements = document.querySelectorAll('.cultivo-info');

cultivoInfoElements.forEach(cultivo => {
    cultivo.addEventListener('click', () => {
        cultivo.classList.toggle('active');
        const content = cultivo.querySelector('p');
        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + 'px';
        }
    });
});

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        const section = document.querySelector(this.getAttribute('href'));
        section.scrollIntoView({
            behavior: 'smooth'
        });
    });
});

function toggleText(cultivo) {
    const description = document.getElementById(cultivo).getElementsByClassName('cultivo-description')[0];
    description.style.display = (description.style.display === 'none' || description.style.display === '') ? 'block' : 'none';
}

function mostrarFertilizantes() {
    var x = document.getElementById("fertilizantesContent");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
        ocultarDescripciones();
    }
}

function mostrarDescripcion(numFertilizante) {
    ocultarDescripciones();
    var descripcionFertilizante = document.getElementById(`descripcionFertilizante${numFertilizante}`);
    descripcionFertilizante.style.display = "block";
}

function ocultarDescripciones() {
    var descripciones = document.querySelectorAll('.opcion-fertilizante p');
    descripciones.forEach(descripcion => {
        descripcion.style.display = 'none';
    });
}
