document.getElementById("inputFile").addEventListener("change", function () {
    let container = document.getElementById('block-container');

	var file = new FileReader();
	file.onload = () => {
		let json = JSON.parse(file.result);
		for (var key in json) {
			var entry = document.createElement('p');
            entry.innerHTML = key + ': <span style="color: #4a60ce">' + json[key] + '</span>';
            container.appendChild(entry)
		}
	};
	file.readAsText(this.files[0]);
});
