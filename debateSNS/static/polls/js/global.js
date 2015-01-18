/**
 * process the news text in the index page.
 */
function omit_text() {
	var omit = $('span.omit');
	omit.each(function() {
		var text = $(this).html().trim();
		var i = 0;
		var count = 0;
		while(count < 15 && !isNaN(text.charCodeAt(i))) {
			if (text.charCodeAt(i) <= 255)
				count += 0.5;
			else
				count += 1;
				
			i++;			
		}
		if (count >= 15) {
			text = text.substr(0, i) + '...';
			$(this).html(text);
		}
	});

	var wide = 0;
	omit.each(function() {
		if ($(this).width() > wide)
			wide = $(this).width();
	});

	omit.each(function() {
		$(this).width(wide);
	});
}

function index_padding_pannel() {
	var uls = $('.introduction .panel-body ul');
	uls.each(function() {
		var lis = $(this).find('li');
		if (lis.length < 5) {
			var remain = 5 - lis.length;
			var blank_li = '<br />';
			var li = '';
			for (var i = 0; i < remain; i++)
				li += blank_li;
				
			$(this).append(li);
		}
	});
}

function gen_pagination() {
	var total_pages = parseInt($('#total_pages').val());
	var current_page = parseInt($('#current_page').val());
	var ul = '';

		var omit = '<li><a href="#"  data-page="0">' + '...' + '</a></li>';
		var last_pre = '<li><a href="#"  data-page="' + (total_pages - 1) + '">' + (total_pages - 1) + '</a></li>';
		var last = '<li><a href="#"  data-page="' + total_pages + '">' + total_pages + '</a></li>';		
		var first_next = '<li><a href="#"  data-page="' + 2 + '">' + 2 + '</a></li>';
		var first = '<li><a href="#"  data-page="' + 1 + '">' + 1 + '</a></li>';
	
	if (total_pages <= 10) {		
		for (var i = 1; i <= total_pages; i++) {
			var li = '';
			if (current_page == i)
				li = '<li class="active"><a href="#"  data-page="' + i + '">' + i + '</a></li>';
			else
				li = '<li><a href="#"  data-page="' + i + '">' + i + '</a></li>';
			ul += li;
		}
	} else if(current_page - 2 <= 2) {
		for (var i = 1; i <= 8; i++) {
			var li = '';
			if (current_page == i)
				li = '<li class="active"><a href="#"  data-page="' + i + '">' + i + '</a></li>';
			else
				li = '<li><a href="#"  data-page="' + i + '">' + i + '</a></li>';
			ul += li;
		}			
		ul = ul  + omit + last_pre + last;
	} else if (current_page + 2 >= total_pages - 1) {
		for (var i = total_pages - 8 + 1; i <= total_pages; i++) {
			var li = '';
			if (current_page == i)
				li = '<li class="active"><a href="#"  data-page="' + i + '">' + i + '</a></li>';
			else
				li = '<li><a href="#"  data-page="' + i + '">' + i + '</a></li>';
			ul += li;
		}		
		ul = first + first_next + omit + ul;
	} else {
		for (var i = current_page - 2; i <= current_page + 2; i++) {
			var li = '';
			if (current_page == i)
				li = '<li class="active"><a href="#"  data-page="' + i + '">' + i + '</a></li>';
			else
				li = '<li><a href="#"  data-page="' + i + '">' + i + '</a></li>';
			ul += li;
		}		
		ul = first + first_next + omit + ul + omit + last_pre + last;
	}
	
	var pre = '';
	var next = '';
	if (current_page == 1)
    	pre = '<li class="disabled"><a href="#"  data-page="0">«</a></li>';
    else
    	pre = '<li><a href="#"  data-page="' + (current_page - 1) + '">«</a></li>';
    	
    if (current_page == total_pages)
    	next = '<li class="disabled"><a href="#"  data-page="0">»</a></li>';
    else
    	next = '<li><a href="#"  data-page="' + (current_page + 1) + '">»</a></li>';
    		
    ul = pre + ul + next;
	$('.news_list_p').html(ul);
	
	//Prevent the default action of the links.
	$('.news_list_p li a').click(function(e) {
		e.preventDefault();
	});
	
	//Replace the table content and regenerate the pangination.
	$('.news_list_p li a').not("a[data-page='0']").click(function() {
		var page = parseInt($(this).attr('data-page'));
		$.get("/news", {
			"page" : page
		}, function(data) {
			var table = $(data).find('.news_list_t');
			var total_pages = $(data).find('#total_pages').val();
			var current_page = $(data).find('#current_page').val();
			$('.news_list_t').replaceWith(table);
			$('.news_list_p').empty();
			$('#total_pages').val(total_pages);
			$('#current_page').val(current_page);
			gen_pagination();
		});
	}); 

}

function gen_us_li() {
	var color = ['bg-lightRed', 'bg-lightGreen', 'bg-lightBlue', 'bg-lightOrange', 'bg-darkViolet', 
					'bg-lightTeal', 'bg-grayLight', 'bg-darkBrown', 'bg-black', 'bg-lightPink', 'bg-darkCobalt'];
	var titles = $('#us_ul').attr('data-lis').split(' ');
	for (var i = 0; i < titles.length; i++) {
		var li = '<li class="stick ' + color[i % 10] +'"><a href="#">' + titles[i]  + '</a></li>';
		$('#us_ul').append(li);
	}
}

function get_info_about_us() {
	$('#us_ul li a').click(function(e) {
		e.preventDefault();
	});
	
	$('#us_ul li').not('.title').click(function() {
		$(this).addClass('active').siblings().removeClass('active');
		var title = $(this).find('a').html().trim();
		$.get('/us', {'title': title}, function(data) {
			$('#us_heading h2').html(data.title);
			$('#us_content').html(data.content);
		});
	});
	
	$('#us_ul li:nth-child(2)').click();
}


function enable_transform() {
	$('.metro .tile').attr('data-click', 'transform');
}
