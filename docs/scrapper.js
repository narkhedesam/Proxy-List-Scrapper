 var width = (window.innerWidth > 0) ? window.innerWidth : screen.width;
 var height = (window.innerHeight > 0) ? window.innerHeight : screen.height;

function scroll(){
	document.getElementById("intro").style.width = "calc(100%)";
	document.getElementById("intro").style.height = ((window.innerHeight > 0) ? window.innerHeight : screen.height )+ 'px';
	
	document.getElementById("home").style.width = "calc(100%)";
	document.getElementById("home").style.height = ((window.innerHeight > 0) ? window.innerHeight : screen.height )+ 'px';
	
	document.getElementById("result_div").style.width = "calc(100%)";
	document.getElementById("result_div").style.height = ((window.innerHeight > 0) ? window.innerHeight : screen.height )+ 'px';
	
	document.getElementById("author").style.width = "calc(100%)";
	document.getElementById("author").style.height = ((window.innerHeight > 0) ? window.innerHeight : screen.height )+ 'px';
	
}

document.addEventListener('DOMContentLoaded', function() {
	document.getElementById("intro").style.width = "calc(100%)";
	document.getElementById("intro").style.height = ((window.innerHeight > 0) ? window.innerHeight : screen.height )+ 'px';
	
	document.getElementById("home").style.width = "calc(100%)";
	document.getElementById("home").style.height = ((window.innerHeight > 0) ? window.innerHeight : screen.height )+ 'px';
	
	document.getElementById("result_div").style.width = "calc(100%)";
	document.getElementById("result_div").style.height = ((window.innerHeight > 0) ? window.innerHeight : screen.height )+ 'px';
	
	document.getElementById("author").style.width = "calc(100%)";
	document.getElementById("author").style.height = ((window.innerHeight > 0) ? window.innerHeight : screen.height )+ 'px';
	
	const labels = document.querySelectorAll('.label');
	labels.forEach(label => {
	  const chars = label.textContent.split('');
	  label.innerHTML = '';
	  chars.forEach(char => {
		label.innerHTML += `<span>${char === ' ' ? '&nbsp' : char}</span>`;
	  });
	})
	
	var clipboard = new ClipboardJS(document.getElementById("copy"));
	
	var scrape_now_button = document.getElementById('scrape_now');
	scrape_now_button.addEventListener('click', function() {
		console.log("scrape button is clicked")
		
		scrape_now_button.classList.add('spin');
		scrape_now_button.disabled = true;

		var category = document.querySelector('input[name="options"]:checked').value;
		var categories = {
			'SSL': 'https://www.sslproxies.org/',
			'GOOGLE': 'https://www.google-proxy.net/',
			'ANANY': 'https://free-proxy-list.net/anonymous-proxy.html',
			'UK': 'https://free-proxy-list.net/uk-proxy.html',
			'US': 'https://www.us-proxy.org/',
			'NEW': 'https://free-proxy-list.net/',
			'SPYS.ME': 'https://spys.me/proxy.txt',
			'proxyscrape': 'https://api.proxyscrape.com/?request=getproxies&proxytype=all&country=all&ssl=all&anonymity=all',
			'ALL': 'ALL'
		}
		
		category_handler(category, categories)

	}, false);
	
	var back = document.getElementById('back');
	back.addEventListener('click', function() {
		scrape_now_button.classList.remove('spin');
		scrape_now_button.disabled = false;
		document.getElementById('result').value = "";
		document.getElementById("result_div").style.display = "none";
		document.getElementById("home").style.display = "block";
	}, false);
	
}, false);


async function category_handler(category, categories){
	var proxyList = []
	if(category == categories.ALL){
		
		/* get proxies from all categories */
		for (var key of Object.keys(categories)){
			if (key != 'ALL'){
				console.log("Getting proxies -> " + key)
				proxies = await get_proxies(categories, key)
				proxyList = proxyList.concat(proxies)
			}
		}
	
	}else{
	
		/* get proxy of an category provided by user */
		proxies = await get_proxies(categories, category)
		proxyList = proxyList.concat(proxies)
	}
	// console.log("proxyList --> " + proxyList)
	try{
		document.getElementById('result').value = proxyList.join("\n")
		document.getElementById("result_div").style.display = "block";
		document.getElementById("home").style.display = "none";
	}catch(e){}
}

async function get_proxies(categories, category){
	/* get proxies from category.*/
	
	return await http_request(categories[category]).then(function(result) {
		//console.log("data --> " + result)
		var proxies = [];
		if (category == 'SPYS.ME' || category == 'proxyscrape'){
			var matches = result.match(/\d+\.\d+\.\d+\.\d+:\d+/g);
			if (matches != null){
				proxies = [].concat(matches)
			}
		} else{
			var matches = result.match(/\d+\.\d+\.\d+\.\d+<\/td><td>\d+/g);
			var proxies = [];
			if (matches != null){
				matches.forEach(function (item, index) {
					proxies.push(item.replace("</td><td>",":"));
				})
			}
		}
		return proxies;
	});
		
}

async function http_request(url){
	
	return await fetch("https://cors-anywhere.herokuapp.com/" + url, {
		method: 'GET', 
	})
	.then(response => response.text())
	.then(data => {
		// console.log("data --> " + data)
		return data;
	})
	.catch((error) => {
		console.error('Error:In http request', error);
		return ""
	});

}