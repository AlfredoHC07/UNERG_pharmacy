// Seleccionamos el formulario
const form = document.querySelector("form");


// Helper function to validate input values based on a regex
function validateInput(value, regex) {
  return regex.test(value);
}

function mostrarError(campo, mensaje) {
  // Eliminamos los errores existentes
  eliminarError(campo);
  // Agregamos la clase 'is-invalid' al campo
  campo.classList.add("is-invalid");
  // Creamos un nuevo mensaje de error y lo agregamos al DOM
  const errorDiv = document.createElement("div");
  errorDiv.className = "invalid-feedback";
  errorDiv.innerText = mensaje;
  campo.parentNode.appendChild(errorDiv);
}

function eliminarError(campo) {
  // Removemos clase 'is-invalid' del campo
  campo.classList.remove("is-invalid");
  // Buscamos y eliminamos los mensajes de error existentes
  const errors = campo.parentNode.querySelectorAll(".invalid-feedback");
  errors.forEach((error) => {
    campo.parentNode.removeChild(error);
  });
}

// Función para validar el formulario
function validarFormulario(evento) {
    // Cancelamos el envío del formulario
    evento.preventDefault();

    // Obtenemos los valores de los campos
    const username = document.querySelector("#username").value.trim();
    const name = document.querySelector("#Name").value.trim();
    const lastName = document.querySelector("#LastName").value.trim();
    const email = document.querySelector("#Email").value.trim();
    const password = document.querySelector("#Password").value.trim();
    const dni = document.querySelector("#Dni").value.trim();
    const phone = document.querySelector("#Phone").value.trim();
    const terms = document.querySelector("#Terms").checked;
    
    // Validamos cada campo
    if (username === "") {
      mostrarError(
        document.querySelector("#username"),
        "Por favor, ingrese un nombre de usuario"
      );
      return;
    } else {
      eliminarError(document.querySelector("#username"));
    }

    if (name === "") {
      mostrarError(
        document.querySelector("#Name"),
        "Por favor, ingrese un nombre"
      );
      return;
    } else {
      eliminarError(document.querySelector("#Name"));
    }

    if (lastName === "") {
      mostrarError(
        document.querySelector("#LastName"),
        "Por favor, ingrese un apellido"
      );
      return;
    } else {
      eliminarError(document.querySelector("#LastName"));
    }

    if (email === "") {
      mostrarError(
        document.querySelector("#Email"),
        "Por favor, ingrese una dirección de correo electrónico"
      );
      return;
    } else if (!validateInput(email, /^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,63}(\.[a-zA-Z]{2,63})?)$/
    )) {
      mostrarError(
        document.querySelector("#Email"),
        "Por favor, ingrese una dirección de correo electrónico válida"
      );
      return;
    } else {
      eliminarError(document.querySelector("#Email"));
    }

      if (password === "") {
        mostrarError(
          document.querySelector("#Password"),
          "Por favor, ingrese una contraseña"
        );
        return;
      } else if (!validateInput(
        password,
        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z]).{8,}$/
      )) {
        mostrarError(
          document.querySelector("#Password"),
          "La contraseña debe tener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial."
        );
        return;
      } else if (password.length < 8) {
        mostrarError(
          document.querySelector("#Password"),
          "La contraseña debe tener al menos 8 caracteres"
        );
        return;
      } else {
        eliminarError(document.querySelector("#Password"));
      }

    if (dni === "") {
      mostrarError(
        document.querySelector("#Dni"),
        "Por favor, ingrese un número de documento"
      );
      return;
    } else if (!validateInput(dni, /^[VE]-\d{6,8}$/)) {
      mostrarError(
        document.querySelector("#Dni"),
        "Por favor, ingrese un número de documento válido (V-XXXXXX o E-XXXXXXX)"
      );
      return;
    } else {
      eliminarError(document.querySelector("#Dni"));
    }

    if (phone === "") {
      mostrarError(
        document.querySelector("#Phone"),
        "Por favor, ingrese un número de teléfono"
      );
      return;
    } else if (!validateInput(phone, /^(0412|0414|0416|0424|0426|0417|0422)\d{7}$/)) {
      mostrarError(
        document.querySelector("#Phone"),
        "Por favor, ingrese un número telefónico en formato válido (04XXXXXXXXX)"
      );
      return;
    } else {
      eliminarError(document.querySelector("#Phone"));
    }

    if (!terms) {
      mostrarError(
        document.querySelector("#Terms"),
        "Por favor, acepte los términos y condiciones"
      );
      return;
    } else {
      eliminarError(document.querySelector("#Terms"));
    }

    // Si todos los campos son válidos, enviamos el formulario
    form.submit();
}

// Asignamos la función validarFormulario al evento submit del formulario
form.addEventListener("submit", validarFormulario);

// Asignamos la función eliminarError a los eventos blur y input de cada campo
document.querySelector("#username").addEventListener("blur", function () {
  if (this.value.trim() === "") {
    mostrarError(this, "Por favor, ingrese un nombre de usuario");
  } else {
    eliminarError(this);
  }
});

document.querySelector("#Name").addEventListener("blur", function () {
  if (this.value.trim() === "") {
    mostrarError(this, "Por favor, ingrese un nombre");
  } else {
    eliminarError(this);
  }
});

document.querySelector("#LastName").addEventListener("blur", function () {
  if (this.value.trim() === "") {
    mostrarError(this, "Por favor, ingrese un apellido");
  } else {
    eliminarError(this);
  }
});

document.querySelector("#Email").addEventListener("blur", function () {
  if (this.value.trim() === "") {
    mostrarError(
      this,
      "Por favor, ingrese una dirección de correo electrónico"
    );
  } else {
    eliminarError(this);
  }
});


document.querySelector("#Password").addEventListener("blur", function () {
  const password = this.value;

  if (password.trim() === "") {
    mostrarError(this, "Por favor, ingrese una contraseña");
  } else if (!validateInput(
    password,
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z]).{8,}$/
  )) {
    mostrarError(
      this,
      "La contraseña debe tener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial."
    );
  } else if (password.length < 8) {
    mostrarError(
      this,
      "La contraseña debe tener al menos 8 caracteres"
    );
  } 
  else {
    eliminarError(this);
  }
});

document.querySelector("#Dni").addEventListener("blur", function () {
  if (!validateInput(this.value.trim(),/^[VE]-\d{6,8}$/)) {
    mostrarError(
      this,
      "Por favor, ingrese una cédula válido (V-XXXXXX o E-XXXXXXX)"
    );
  } else {
    eliminarError(this);
  }
});

document.querySelector("#Phone").addEventListener("blur", function () {
  if (!validateInput(this.value.trim(),/^(0412|0414|0416|0424|0426|0417|0422)\d{7}$/)) {
    mostrarError(this, "Por favor, ingrese un número telefónico válido");
  } else {
    eliminarError(this);
  }
});