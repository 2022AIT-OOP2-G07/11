
const btn = document.querySelector('button');
const input = document.querySelector('input');
const afterUpload = () => {
    btn.disabled = false;
    btn.value = "アップロード";
    input.value = "";
    formData = new FormData();
}

btn.addEventListener('click', (e) => {
    e.preventDefault();
    const file = input.files[0];
    if (file === undefined) {
        alert("ファイルが選択されていません");
        return;
    }
    const formData = new FormData();
    btn.disabled = true;
    btn.value = "アップロード中"
    formData.append("img_file", file);
    fetch('/upload',{
        method: "POST",
        body: formData
    }).then(res => {
    res.json().then(data => {
        if (data.status === 'false') {
            alert(data.message);
        } else if (data.status === 'true') {
            alert("送信が完了しました");
        } else {
            alert("ファイルサイズが1MBを超えています");
        }
        afterUpload();
    });
    });
});