let submit = document.getElementById('submit');

submit.onclick = get_data;

function get_data() {
    let spm1 = document.getElementById('spm1').value;
    let spm2 = document.getElementById('spm2').value;
    let spm3 = document.getElementById('spm3').value;
    let spm4 = document.getElementById('spm4').value;
    let spm5 = document.getElementById('spm5').value;
    let spm6 = document.getElementById('spm6').value; 

    // legger input-data i en array for å kjøre alt gjennom en for løkke
    // fremfor å sjekke hvert svar individuelt
    // dette gjør det også lettere å legge inn flere svar senere 
    let data = [
        spm1,
        spm2,
        spm3,
        spm4,
        spm5,
        spm6,
    ];

    let answers = [
        'onedrive',
        'sharepoint',
        'y',
        'n',
        'onedrive/teams',
        'y',
    ];
    
    // sjekker hvor mange rette svar 
    max_correct = 6;
    correct_answers = 0;
    for (let i = 0; i < data.length; i++) {
        if (data[i] == answers[i]) {
            correct_answers += 1;
        }
    }
    
    let score = 'Du fikk: ' + correct_answers + '/' + max_correct + '. ';
    let msg = '';
    if (correct_answers > 4) {
        msg += 'Gratulerer, du er nå sertifisert hjemmearbeider.';
    } else {
        msg += 'Du bestod ikke. Kontakt support ved å sende en ticket.';
    }

    let final_sentence = score + msg;

    alert(final_sentence)
}

function goHome() {
    window.location.href = '/';
}