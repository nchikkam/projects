d3.json("json/resume.json", function(a, b) {
    //Header Section
    email = d3.select('#email');
    email.text(b.header.email);

    phone = d3.select('#phone');
    phone.text(b.header.phone);

    d3.select("#name").text(b.header.firstname);
    d3.select("#educationHeading").text("Education");
    d3.select("#openSourceHeading").text("OpenSource");
    d3.select("#experienceHeading").text("Experience");

    d3.select("#talents").text(b.header.talents.join(" "));
    var items = b.experience.items;

    // Experience Section
    exps = d3.select("#exps")
        .selectAll("ul")
        .data(items)
        .enter()
        .append("ul")
        .append("li")
        .each(function(d, i){
            d3.select(this).selectAll("div")
                .data(['title', 'duration', 'organisation'])
                .enter()
                .append("div")
                .attr("id", function(id){return id;})
                .text(function(g){return items[i][g];})
        }
        );
    // Projects
    exps.each(function(d, i){
        d3.select(this).selectAll("ul")
        .data(d.projects)
        .enter()
        .append("ul")
        .append("li")
        .text(function(d, i){return d;})
    });
    // Tools Used
    exps.append("ul")
        .append("li")
        .text(function(d){return d.technologies.tools.join(" ");
        });

    //education
    d3.select("#education")
        .selectAll("ul")
        .data(b.education)
        .enter()
        .append("ul")
        .append("li")
        .text(function(d, i){return b.education[i];});

    // Open source contributions
    d3.select("#opensource")
        .selectAll("ul")
        .data(b.opensource)
        .enter()
        .append("ul")
        .append("li")
        .text(function(d, i){
            return b.opensource[i];
        });
    }
);