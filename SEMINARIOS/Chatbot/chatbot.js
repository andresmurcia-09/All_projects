const chatBody = document.getElementById("chat-body");
const userInputElement = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");

const responses = {
    "hola": "¡Hola! En qué puedo ayudarte",
    "cuéntame más sobre tu negocio": "Somos una empresa que se especializa en proporcionar soluciones de chatbot para ayudar a las empresas a adaptarse a las necesidades cambiantes generadas por la pandemia de COVID-19",
    "qué tipos de chatbots ofrecen": "Ofrecemos chatbots empresariales altamente personalizables que se adaptan a las necesidades específicas de cada empresa Estos chatbots pueden utilizarse en diversas industrias, incluyendo el comercio electrónico, las instituciones financieras y las compañías de servicios",
    "cómo funcionan sus planes de suscripción": "Tenemos diferentes planes de suscripción para adaptarnos a las necesidades de nuestros clientes Ofrecemos tarifas flexibles que varían según el plan y la cantidad de transacciones Nuestros planes incluyen características como soporte técnico 24/7 y personalización",
    "cómo se integra el chatbot en mi sitio web": "La integración es sencilla Proporcionamos instrucciones detalladas y soporte técnico para ayudar a su empresa a implementar el chatbot en su sitio web existente",
    "cuáles son los beneficios de utilizar un chatbot empresarial": "Nuestros chatbots mejoran la eficiencia operativa, ahorran tiempo y recursos, optimizan la atención al cliente y se adaptan a las necesidades cambiantes También pueden reducir costos operativos y aumentar la rentabilidad",
    "cómo se personaliza el chatbot para mi empresa": "Nuestros chatbots son altamente personalizables Trabajamos estrechamente con su empresa para adaptar el chatbot a sus necesidades específicas, incluyendo el lenguaje y las interacciones específicas de su industria",
    "ofrecen pruebas gratuitas": "Sí, ofrecemos pruebas gratuitas para que su empresa pueda experimentar los beneficios de nuestros chatbots antes de comprometerse con un plan de suscripción",
    "cuál es su política de seguridad de datos": "La seguridad de los datos es una prioridad Implementamos medidas de seguridad robustas para proteger la información de su empresa y sus clientes",
    "cómo puedo ponerme en contacto con su equipo de soporte": "Puede ponerse en contacto con nuestro equipo de soporte las 24 horas del día, los 7 días de la semana a través de nuestro servicio de chat en vivo o por correo electrónico",
    "qué tecnología utilizan para desarrollar los chatbots": "Utilizamos tecnologías de vanguardia, incluyendo inteligencia artificial y aprendizaje automático, para desarrollar chatbots eficientes y efectivos",
    "cuál es la duración de los contratos de suscripción": "Ofrecemos planes de suscripción flexibles Puede elegir entre contratos mensuales o anuales, según sus preferencias",
    "qué empresas ya han utilizado sus servicios": "Hemos trabajado con empresas en diversas industrias, incluyendo nombres conocidos en el comercio electrónico, las instituciones financieras y las compañías de servicios",
    "ofrecen capacitación para utilizar el chatbot": "Sí, proporcionamos capacitación a su equipo para asegurarnos de que pueda utilizar el chatbot de manera efectiva",
    "cuál es el costo de los planes de suscripción": "Los costos varían según el plan y la cantidad de transacciones Contáctenos para obtener una cotización personalizada",
    "qué idiomas son compatibles con su chatbot": "Nuestro chatbot es compatible con múltiples idiomas para satisfacer las necesidades de su audiencia global",
    "cómo se actualizan los chatbots" : "Realizamos actualizaciones periódicas para garantizar que su chatbot esté al día con las últimas tendencias y tecnologías",
    "ofrecen soporte técnico en horario no laboral": "Sí, nuestro equipo de soporte está disponible las 24 horas del día para atender sus consultas y problemas",
    "qué ventajas específicas ofrece su chatbot para el comercio electrónico": "Para el comercio electrónico, nuestro chatbot puede mejorar la experiencia del cliente, agilizar el proceso de compra y ofrecer soporte personalizado",
    "cómo se personalizan las interacciones con los clientes": "Personalizamos las interacciones para satisfacer las necesidades de su empresa y sus clientes, brindando respuestas específicas y contextuales",
    "cuál es el tiempo de implementación típico para un chatbot" : "El tiempo de implementación varía según la complejidad del proyecto, pero trabajamos eficientemente para poner su chatbot en funcionamiento lo más rápido posible",

};


function displayResponse(message, isUser = false) {
    const messageElement = document.createElement("div");
    messageElement.className = `chat-message ${isUser ? "user" : "bot"}`;
    messageElement.innerText = message;
    chatBody.appendChild(messageElement);
}

function handleUserInput() {
    const userMessage = userInputElement.value;
    userInputElement.value = "";
    displayResponse(userMessage, true);

    if (responses.hasOwnProperty(userMessage)) {
        const botResponse = responses[userMessage];
        displayResponse(botResponse);
    } else {
        displayResponse("Lo siento, no entiendo esa pregunta. ¿Puedes intentar con otra?");
    }
}

sendButton.addEventListener("click", handleUserInput);
userInputElement.addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        handleUserInput();
    }
});

