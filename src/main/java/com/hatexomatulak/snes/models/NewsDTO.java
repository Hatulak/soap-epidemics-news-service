package com.hatexomatulak.snes.models;

import com.project.xml.news.News;
import lombok.*;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import java.util.Date;

@Data
@Entity
@NoArgsConstructor
@AllArgsConstructor
@RequiredArgsConstructor
public class NewsDTO {
    @Id
    @GeneratedValue
    private Long id;
    @NonNull
    private String name;
    @NonNull
    private String desc;
    @NonNull
    private Date date;

    public News castToNews() {
        News news = new News();
        news.setId(id);
        news.setName(name);
        news.setDesc(desc);
        news.setDate(date.toString());
        return news;
    }
}
