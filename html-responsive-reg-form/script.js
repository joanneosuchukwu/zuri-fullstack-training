
function showError(errorElement, errorMessage){
    document.querySelector("."+errorElement).classList.add("display-error");
    document.querySelector("."+errorElement).innerHTML = errorMessage;
}

function clearError(){
    let errors = document.querySelectorAll(".error");
    for(let error of errors){
        error.classList.remove("display-error");
    }
}


let form = document.forms['loginform'];
form.onsubmit = function(event){


    clearError();

    if(form.email.value === ""){
        showError("email-error", "Looks like this is not an email");
        return false;
    }


    if(form.firstname.value === ""){
        showError("firstname-error", "Looks like this is not an email");
        return false;
    }


    if(form.lastname.value === ""){
        showError("lastname-error", "Looks like this is not an email");
        return false;
    }



    if(form.password.value === ""){
        showError("password-error", "Looks like this is not an email");
        return false;
    }



    event.preventDefault();
}