let otpInput = document.querySelectorAll("[name=otp]"); // Get all the inputs.
let verifyOtpBtn = document.getElementsByTagName('button')[0]; // Get verify button.
const pasteBtn = document.querySelector('#paste-btn'); // Get paste button.

// To keep button disabled till all the fields are filled.
const checkInputs = () => {
    let validInputs = Array.from(otpInput).filter( input => input.value !== "");
    if(validInputs.length == 6) {
        verifyOtpBtn.classList.remove("disabled");
    }
}

// To paste OTP from the clipboard on the click of a button.
const pasteOTP = () => {
    let clipboardData = navigator.clipboard.readText(); // Will read content from the clipboard
    clipboardData.then((clipboardText) => {
        const digits = clipboardText.match(/\d+/g); // Checking if the content is in the number format.
        const firstValue = Object.values(digits)[0].split(''); // Getting the recently copied number as a string and splitting it into single digit and storing in an array.
        if (firstValue && firstValue.length > 0) {
            otpInput.forEach((el, index) => {
                if (index <= firstValue.length) {
                    el.value = firstValue[index];
                    otpInput[index + 1]?.focus();
                } else {
                    el.value = '';
                }
            })
            checkInputs();
        }
    })
}
pasteBtn.addEventListener('click', () => {
    pasteOTP();
});

otpInput.forEach((el, index) => {
    // Listen for the "input" event on the input element
    el.addEventListener("input", () => {
        // Get the input value
        let value = el.value;    
        // Remove any non-numeric characters
        value = value.replace(/[^0-9]/g, "");    
        // Limit the input to a single digit
        if (value.length > 1) {
            value = value.slice(0, 1);
        }
        // Set the input value
        el.value = value;
    });
    el.addEventListener('keyup', (event) => {
        // To shift focus to the next input when the single digit is entered to the current one.
        const key = event.key;
        if(el.value.length >= 1 && (key >= 96 || key <= 105)) {
            otpInput[index + 1]?.focus();
        }
        // To go to the previous input when current's value is cleared.
        else if(el.value == '' && key === "Backspace") {
            verifyOtpBtn.classList.add("disabled");
            otpInput[index - 1]?.focus();
        }
        checkInputs();
    })
})

// To pastae OTP using keyboard keys.
otpInput[0].addEventListener("keydown", function (ev) {

    // function to check the detection
    ev = ev || window.event;  // Event object 'ev'
    var key = ev.which || ev.keyCode; // Detecting keyCode
    
    // Detecting Ctrl
    var ctrl = ev.ctrlKey ? ev.ctrlKey : ((key === 17)
        ? true : false);
    
    // If key pressed is V and if ctrl is true.
    if (key == 86 && ctrl) {
        pasteOTP();
    }
    
});

// To get each input value into the one string and then check with the correct OTP.
const form = document.getElementsByTagName('form')[0];
// Reset form when page refreshes.
window.onload = function() {
    form.reset();
    otpInput[0].focus();
}
let fullOtp = [];
let correctOtp = "123456";
let attempts = 0;
form.addEventListener('submit', (e) => {
    e.preventDefault(); // We call e.preventDefault to prevent the default submit behavior so we can do client-side form submission.
    const formData = new FormData(form); // Then we create the formData object with the FormData constructor with the form as the argument to get the form data values.
    for (const pair of formData.entries()) { // And then we call formData.entries to get an array of form data key-pair pairs.
        fullOtp.push(pair[1]);
    }
    let a = fullOtp.join(''); // To get entered OTP as a single string.
    if (a == correctOtp) {
        document.getElementsByTagName('body')[0].innerText = "Entered OTP is correct.";
    }
    else {
        attempts++;
        if (attempts < 3) {
            alert(`Entered OTP is incorrect. You have ${3 - attempts} attempts left. Please retry.`);
            for(let i = 0; i < otpInput.length - 1; i++) {
                if(otpInput[i].value == "") {
                    otpInput[i].focus();
                    break;
                }
            }
            fullOtp = [];
        } else {
            alert("You have exceeded the maximum number of attempts. Please try again later.");
            window.location.reload();
        }
    }
})