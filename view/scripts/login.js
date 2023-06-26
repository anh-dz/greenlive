let loginBtn = document.getElementById("login-btn");

loginBtn.addEventListener("click", () => {
    let email = document.getElementById('email-field').value
    let password = document.getElementById('password-field').value
    if (!email || !password) {
        return
    }
    try {
        let response = fetch("localhost:5000", { 
            method: "POST", 
            headers: { "Content-Type": "application/json" },
            body: { email, password } }).then(res => res.json())
    
        localStorage.setItem('user:name', email)
        localStorage.setItem('user:id', response.id)
        localStorage.setItem('user:point', response.point)
    } catch(e) {
        alert("Email/mật khẩu không trùng khớp. Vui lòng thử lại.")
        return
    }
})