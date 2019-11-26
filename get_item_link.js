<script>
    //아이디어스 페이지에 보이는 아이템들 링크를 가져오는 스크립트 코드
    string = ''
    
    items = $('.ui_grid__item > .ui_card > .ui_card__imgcover > a')
    items.each(function(index, item){
        href = item.getAttribute('href')
        if(index == items.length - 1){ string = string + 'https://www.idus.com/' + href }
        else { string = string + 'https://www.idus.com/' + (href +'\n') }
        
    }); 
    console.log(string)

    
</script>