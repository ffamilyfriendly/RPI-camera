const decodeDate = (d) => {
    d = decodeURIComponent(d)
    const seg1 = d.split("-")
    const time = seg1[seg1.length - 1].replace(/;/gi,":").replace(".png","")
    return `${seg1[0]}/${seg1[1]}/${seg1[2]} <b>at</b> ${time}`
}

document.addEventListener("DOMContentLoaded", async () => {
    console.log("aa")
    const res = await fetch("./images").then(r => r.text())
    const d = new DOMParser().parseFromString(res, "text/html");
    const place = document.getElementById("container")

    d.querySelectorAll("a").forEach(el => {
        const filename = el.getAttribute("href")
        place.innerHTML += `
            <div class="entry">
                <img src="./images/${filename}">
                <p><b>Filename: </b>${filename} <b>date:</b> ${decodeDate(filename)}</p>
            </div>
        `
    })
})