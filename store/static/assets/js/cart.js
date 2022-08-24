var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		var option = this.textContent
		console.log('productId:', productId, 'Action:', action , 'option:', option )
		console.log('USER:', user)

		if (user == 'AnonymousUser'){
			addCookieItem(productId, action, option)
		}else{
			updateUserOrder(productId, action, option)
		}
	})
}

function updateUserOrder(productId, action, option){
	console.log('User is authenticated, sending data...')

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId':productId, 'action':action , 'option':option})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
			if (data.msg === 'success'){
				if (action == 'add') {
					console.log('item added successfully')
				} else {
					console.log('item removed from the cart')
				}
				

			} else {
				console.log('there was an error , try again')
			}
		    
		});
}

function addCookieItem(productId, action, option){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity':1}

		}else{
			cart[productId]['quantity'] += 1
		}
	}
	

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}

	if (action == 'post'){
		cart[productId]['option'] = option
	}
	
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	
}


