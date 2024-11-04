function top_accounts(id, config = {
    "tweetLimit": 10,
}) {

    // initialize the block
    
    function build_top_account(account)
    {
        var container=document.getElementById("accounts_container");
        container.innerHTML='';

        for(let i=0;i<account.length;i++){
            var accountElement=document.createElement("li");
            accountElement.className="account";
            accountElement.innerHTML=account[i].name
            container.appendChild(accountElement);
        }

        
    }
    
    function onEvent(data) {
        build_top_account(data)
        
        // add the tweet to the element
        // but prepend it so that the newest tweet is at the top
    }

    // return the onEvent function
    return onEvent;
}