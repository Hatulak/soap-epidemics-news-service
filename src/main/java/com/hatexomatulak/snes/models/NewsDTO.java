package com.hatexomatulak.snes.models;

import com.project.xml.types.News;
import lombok.*;

import javax.persistence.*;
import java.util.Date;

@Data
@Entity
@NoArgsConstructor
@AllArgsConstructor
@RequiredArgsConstructor
public class NewsDTO {
    @Id
    @GeneratedValue
    private Long newsId;
    @NonNull
    private String name;
    @NonNull
    private String desc;
    @NonNull
    private Date date;
    @ManyToOne()
    @NonNull
    @JoinColumn(name = "categoryId", nullable = false)
    private CategoryDTO category;

    public News castToNews() {
        News news = new News();
        news.setId(newsId);
        news.setName(name);
        news.setDesc(desc);
        news.setDate(date.toString());
        news.setCategoryId(category.getCategoryId());
        news.setCategoryName(category.getName());
        return news;
    }
}
