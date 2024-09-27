window.addEventListener("load", async() => {
    await initialLoad();
})

const initialLoad = async() => {
    submit.addEventListener("click", (event) => {
        calculateMonkey();
    })
}

const calculateMonkey = async() => {
    try {

        // Parámetros iniciales:
        const str = inputText.value;
        loading.innerHTML = "Calculando...";
        result.innerHTML = "";

        // Traer métricas del proceso:
        const response = await fetch(`/process/${str}`)
        const data = await response.json();

        // Mostrar resultados:
        if (data.message == 'success') {
            let result_text = `Después de ${data.data.iters} intentos, el mono logró escribir "${str}" (${data.data.duration} s)`;
            result.innerHTML = result_text;
            loading.innerHTML = "Listo";
        } else {
            alert('No se procesó correctamente el texto. Reviselo. No se permiten valores numéricos');
            loading.innerHTML = "Error";
            result.innerHTML = "";
        }

    } catch (error) {
        console.log(error);
    }
}