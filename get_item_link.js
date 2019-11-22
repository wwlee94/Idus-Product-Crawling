<script>

    string = ''
    
    items = $('.ui_grid__item > .ui_card > .ui_card__imgcover > a')
    items.each(function(index, item){
        href = item.getAttribute('href')
        if(index == items.length - 1) string = string + 'https://www.idus.com/' + href
        else string = string + 'https://www.idus.com/' + (href +'\n')
        
    }); 
    console.log(string)

    
</script>