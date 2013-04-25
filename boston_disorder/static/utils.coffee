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

insertParams = (keys, values) ->
    kvp = document.location.search.substr(1).split('&');
    j = 0
    while j < keys.length
        key = escape(keys[j])
        value = escape(values[j]);

        if value == ""
            j++
            continue

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
        j++

    document.location.search = kvp.join('&')


changeType = (new_type, base) ->
    new_type = escape(new_type);
    if base == "physical"
        other_base = "social"
    else
        other_base = "physical"

    url = document.location.pathname.split('/');

    i=0
    while i < url.length
        if url[i]==base
            if i + 1 == url.length
                url.push new_type
            else
                url[i+1] = new_type
            break
        else if url[i]==other_base
            url[i] = base
            if i + 1 == url.length
                url.push new_type
            else
                url[i+1] = new_type
            break

        i++
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
        changeType("physical_disorder", "physical")

$ ->
    $("#private").click ->
        changeType("private", "physical")

$ ->
    $("#housing").click ->
        changeType("housing", "physical")

$ ->
    $("#uncivil_use").click ->
        changeType("uncivil_use", "physical")

$ ->
    $("#big_buildings").click ->
        changeType("big_buildings", "physical")

$ ->
    $("#public").click ->
        changeType("public", "physical")

$ ->
    $("#graffiti").click ->
        changeType("graffiti", "physical")

$ ->
    $("#trash").click ->
        changeType("trash", "physical")

$ ->
    $("#all_911_calls").click ->
        changeType("all_911_calls", "social")

$ ->
    $("#social_disorder").click ->
        changeType("social_disorder", "social")

$ ->
    $("#public_social_disorder").click ->
        changeType("public_social_disorder", "social")

$ ->
    $("#socstrife").click ->
        changeType("socstrife", "social")

$ ->
    $("#alcohol").click ->
        changeType("alcohol", "social")

$ ->
    $("#violence").click ->
        changeType("violence", "social")

$ ->
    $("#interpersonal_violence").click ->
        changeType("interpersonal_violence", "social")

$ ->
    $("#guns").click ->
        changeType("guns", "social")

$ ->
    $("#medical_emergency").click ->
        changeType("medical_emergency", "social")

$ ->
    $("#major_medical_emergency").click ->
        changeType("major_medical_emergency", "social")

$ ->
    $("#youth_health").click ->
        changeType("youth_health", "social")

$ ->
    $("#no_med").click ->
        changeType("no_med", "social")

$ ->
    $("#i_physical_disorder").click ->
        $('.ui-dialog-titlebar').text("Physical Disorder information")
        $('.ui-dialog-content').html("All physical disoder")
        $("#dialog-message").dialog('open')
        return false

$ ->
    $("#i_private").click ->
        $('.ui-dialog-titlebar').text("Private Neglect information")
        $('.ui-dialog-content').html("Private Neglect indicates deterioration to privately-owned buildings and spaces, or misuse of these spaces that can negatively impact the neighborhood (e.g., illegal rooming house). For more information <a href='/boston/more_info/#private_neglect' target='_blank'>Click Here</a>")
        $("#dialog-message").dialog('open')
        return false

$ ->
    $("#i_housing").click ->
        $('.ui-dialog-titlebar').text("Housing Issues information")
        $('.ui-dialog-content').html("Housing includes nine items referring to poor maintenance by landlords (e.g., poor heating, chronic dampness) and the presence of pests (e.g., bedbugs). For more information <a href='/boston/more_info/#private_neglect' target='_blank'>Click Here</a>")
        $("#dialog-message").dialog('open')
        return false

$ ->
    $("#i_uncivil_use").click ->
        $('.ui-dialog-titlebar').text("Uncivil Use of Space information")
        $('.ui-dialog-content').html("Uncivil Use includes seven items that reflect private residents negatively impacting the public sphere (e.g., illegal rooming house, poor conditions of property, and abandoned building). For more information <a href='/boston/more_info/#private_neglect' target='_blank'>Click Here</a>")
        $("#dialog-message").dialog('open')
        return false

$ ->
    $("#i_big_buildings").click ->
        $('.ui-dialog-titlebar').text("Big Buildings information")
        $('.ui-dialog-content').html("Big Buildings includes three different case types regarding problems with the upkeep of big buildings, like condos. For more information <a href='/boston/more_info/#private_neglect' target='_blank'>Click Here</a>")
        $("#dialog-message").dialog('open')
        return false
        alert()

$ ->
    $("#i_public").click ->
        $('.ui-dialog-titlebar').text("Public Denigration information")
        $('.ui-dialog-content').html("Public Denigration indicates issues that reflect disrespect for the public space, including graffiti and the inappropriate disposal of trash. For more information <a href='/boston/more_info/#public_denigration' target='_blank'>Click Here</a>")
        $("#dialog-message").dialog('open')
        return false

$ ->
    $("#i_graffiti").click ->
        $('.ui-dialog-titlebar').text("Graffiti information")
        $('.ui-dialog-content').html("Graffiti includes two different case types regarding graffiti, one generated by constituents, the other by public works. For more information <a href='/boston/more_info/#public_denigration' target='_blank'>Click Here</a>")
        $("#dialog-message").dialog('open')
        return false

$ ->
    $("#i_trash").click ->
        $('.ui-dialog-titlebar').text("Trash information")
        $('.ui-dialog-content').html("Trash includes five items related to incivilities regarding trash disposal: illegal dumping, improper storage of trash barrels, empty litter basket, abandoned bicycle, and rodent activity.  This last is not itself an incivility, but is a consequence of poor trash storage. For more information <a href='/boston/more_info/#public_denigration' target='_blank'>Click Here</a>")
        $("#dialog-message").dialog('open')
        return false

$ ->
    $("#i_all_911_calls").click ->
        $('.ui-dialog-titlebar').text(" information")
        $('.ui-dialog-content').html("Add information")
        $("#dialog-message").dialog('open')
        return false

$ ->
    $("#i_social_disorder").click ->
        $('.ui-dialog-titlebar').text("Social Disorder information")
        $('.ui-dialog-content').html("All social disorder")
        $("#dialog-message").dialog('open')
        return false

$ ->
    $("#i_public_social_disorder").click ->
        $('.ui-dialog-titlebar').text("Public Social Disorder information")
        $('.ui-dialog-content').html("Public Social Disorder indicates events that reflect social disorder in the public space (e.g., panhandlers). For more information <a href='/boston/more_info/#public_social' target='_blank'>Click Here</a>")
        $("#dialog-message").dialog('open')
        return false

$ ->
    $("#i_socstrife").click ->
        $('.ui-dialog-titlebar').text("Social Strife information")
        $('.ui-dialog-content').html("Social Strife indicates events that reflect interpersonal conflict in the neighborhood (e.g., domestic violence). For more information <a href='/boston/more_info/#social_strife' target='_blank'>Click Here</a>")
        $("#dialog-message").dialog('open')
        return false

$ ->
    $("#i_alcohol").click ->
        $('.ui-dialog-titlebar').text("Alcohol-Related Issues information")
        $('.ui-dialog-content').html("Alcohol-Related Issues indicates events that specifically reference public drunkenness or public consumption of alcohol. For more information <a href='/boston/more_info/#alcohol' target='_blank'>Click Here</a>")
        $("#dialog-message").dialog('open')
        return false

$ ->
    $("#i_violence").click ->
        $('.ui-dialog-titlebar').text("Violence information")
        $('.ui-dialog-content').html("All violence")
        $("#dialog-message").dialog('open')
        return false

$ ->
    $("#i_interpersonal_violence").click ->
        $('.ui-dialog-titlebar').text("Interpersonal Violence information")
        $('.ui-dialog-content').html("Interpersonal Violence indicates events that reflect interpersonal violence that do not involve a gun (e.g., fight). For more information <a href='/boston/more_info/#interpersonal_violence' target='_blank'>Click Here</a>")
        $("#dialog-message").dialog('open')
        return false

$ ->
    $("#i_guns").click ->
        $('.ui-dialog-titlebar').text("Prevalence of Guns information")
        $('.ui-dialog-content').html("Prevalence of Guns indicates events that involve the use of guns (e.g., shooting). For more information <a href='/boston/more_info/#guns' target='_blank'>Click Here</a>")
        $("#dialog-message").dialog('open')
        return false

$ ->
    $("#i_medical_emergency").click ->
        $('.ui-dialog-titlebar').text("Medical Emergencies information")
        $('.ui-dialog-content').html("All medical emergencies")
        $("#dialog-message").dialog('open')
        return false

$ ->
    $("#i_major_medical_emergency").click ->
        $('.ui-dialog-titlebar').text("Major Medical Emergencies information")
        $('.ui-dialog-content').html("Major Medical Emergencies indicates events that reflect major medical emergencies (e.g., stroke). For more information <a href='/boston/more_info/#major_medical' target='_blank'>Click Here</a>")
        $("#dialog-message").dialog('open')
        return false

$ ->
    $("#i_youth_health").click ->
        $('.ui-dialog-titlebar').text("Youth Health Emergencies information")
        $('.ui-dialog-content').html("Youth Health Emergencies indicates events that reflect medical emergencies surrounding birth and young children (e.g., ob-gyn). For more information <a href='/boston/more_info/#youth_health' target='_blank'>Click Here</a>")
        $("#dialog-message").dialog('open')
        return false

$ -> 
    $("#dialog-message").dialog({
        autoOpen: false,
        modal: true,
        width: 300, 
        position: ['center', 80]
        buttons: {
        Ok: ->
          $( this ).dialog( "close" )
        }
    })



$ ->
    $("#help").click ->
        old_display = $("#help_modal")[0].style.display
        if old_display == 'none'
            $("#help_modal")[0].style.display = "block"
        else
            $("#help_modal")[0].style.display = "none"

$ ->
    $("#apply").click ->
        params = []
        values = []

        if document.location.pathname.indexOf('physical') == -1
            start = 'f_close_dt__gte'
            end = 'f_close_dt__lte'
        else
            start = 'f_open_dt__gte'
            end = 'f_open_dt__lte'

        sd = $("#start_date").datepicker("getDate");
        s_date = ""
        if sd
            s_year = sd.getFullYear()
            s_month = sd.getMonth()+1
            s_day = sd.getDate()
            s_date = s_year+"-"+s_month+"-"+s_day
            params.push start
            values.push s_date

        ed = $("#end_date").datepicker("getDate");
        e_date = ""
        if ed
            e_year = ed.getFullYear()
            e_month = ed.getMonth()+1
            e_day = ed.getDate()
            e_date = e_year+"-"+e_month+"-"+e_day
            params.push end
            values.push e_date

        f_type = $("#f_type").val()
        f_val = $("#f_val").val()

        if f_type and f_val
            params.push "f_"+f_type
            values.push f_val

        f_compare_val = $("#f_nsa_name__in").val()
        if f_compare_val
            params.push "f_nsa_name__in"
            values.push "list("+f_compare_val+")"

        insertParams(params, values)
       
$ ->
    $("#toggle_numbers").click ->
        if mc.getMarkers().length == 0
            mc.addMarkers(markersArray)
        else
            mc.clearMarkers()
        #if mc.map == null
        #    mc.setMap(map)
        #    mc.redraw()
        #else
        #    mc.setMap(null)
        #    mc.redraw()

$ ->
    $("#toggle_cbgs").click ->
        if block_groups.map == null
            block_groups.setMap(map)
        else
            block_groups.setMap(null)
$ ->
    $("#toggle_neighborhoods").click ->
        if neighborhoods.map == null
            neighborhoods.setMap(map)
        else
            neighborhoods.setMap(null)
$ ->
    $("#toggle_bowdoin_geneva").click ->
        if bowdoin_geneva.map == null
            bowdoin_geneva.setMap(map)
        else
            bowdoin_geneva.setMap(null)
