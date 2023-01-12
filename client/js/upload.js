const upload = (e) => {
    var data = new FormData()
    data.append('file', e.target.files[0])
    fetch('http://localhost:5000/upload', {
        method: "POST", 
        body: data
    })
}

const checkHealth = async() => {
    await fetch('http://localhost:5000/health', {
        method: "GET", 
    })
}