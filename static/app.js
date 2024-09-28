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

        // Parámetro inicial:
        const str = inputText.value;

        // Cambios en pantalla y probabilidad:
        const response_0 = await fetch(`/process/${str}/probab`)
        const data_0 = await response.json();
        if (data.message == 'success') {
            loading.innerHTML = "Calculando...";
            probab.innerHTML = `La probabilidad de que el mono tipee "${str}" es de 1 en ${data_0.probab}`;
            result.innerHTML = "";
        } else {
            alert('No se procesó correctamente el texto. Reviselo. No se permiten valores numéricos');
            loading.innerHTML = "Error";
            result.innerHTML = "";
        }

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