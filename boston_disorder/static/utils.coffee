insertParam = (key, value) ->
    key = escape(key)
    value = escape(value);

    kvp = document.location.search.substr(1).split('&');

    i=kvp.length
    x
    while i--
        x = kvp[i].split('=')
        if (x[0]==key)
            x[1] = value
            kvp[i] = x.join('=')
            break

    if i<0 
        kvp[kvp.length] = [key,value].join('=')

    document.location.search = kvp.join('&')

changeType = (new_type) ->
    new_type = escape(new_type);

    url = document.location.pathname.split('/');

    console.log(url)

    i=0
    while i < url.length
        if (url[i]=="crm")

            if i + 1 == url.length
                url.push new_type
            else
                url[i+1] = new_type
            break
        i++
    console.log(url)
    document.location.pathname = url.join('/')

$ ->
	$("#change_map").click ->
        url = window.location.pathname
        if url.indexOf("tree_map") != -1
            url = url.replace("tree_map", "map")
        else
            url = url.replace("map", "tree_map")
        
        window.location.href = url
        #window.location.reload()

$ ->
    $("#census_tract").click ->
        insertParam("granularity","Census Tract")

$ ->
    $("#block_group").click ->
        insertParam("granularity","Block Group")

$ ->
    $("#block").click ->
        insertParam("granularity","Block")

$ ->
    $("#address").click ->
        insertParam("granularity","Address")

$ ->
    $("#heat_map").click ->
        insertParam("map_type","heat_map")

$ ->
    $("#markerclusterer").click ->
        insertParam("map_type","markerclusterer")

$ ->
    $("#circles").click ->
        insertParam("map_type","circles")

$ ->
    $("#physical_disorder").click ->
        changeType("physical_disorder")

$ ->
    $("#private").click ->
        changeType("private")

$ ->
    $("#housing").click ->
        changeType("housing")

$ ->
    $("#uncivil_use").click ->
        changeType("uncivil_use")

$ ->
    $("#big_buildings").click ->
        changeType("big_buildings")

$ ->
    $("#public").click ->
        changeType("public")

$ ->
    $("#graffiti").click ->
        changeType("graffiti")

$ ->
    $("#trash").click ->
        changeType("trash")

save_filter: (text) ->
	$.ajaxQueue
        url: window.location.pathname,
        type: "GET",
        success: -> 
            console.log "success"
        error: (data) ->
            alert("Save Failed: "+data.responseText)
        complete: ->
            window.location.reload()