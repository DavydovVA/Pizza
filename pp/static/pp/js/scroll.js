function objScroll(url, pages, id) {
    let page = 1;

    function scroll() {
        if ((window.innerHeight + window.scrollY) >= document.body.scrollHeight && page < pages) {
            page++;

            let objects = document.getElementById(id);

            let request = new XMLHttpRequest();
            request.open('GET', url + '?page=' + page.toString());
            request.send();
            request.onload = function () {
                objects.innerHTML += request.responseText;
            }

        }
    }

    return scroll

}
