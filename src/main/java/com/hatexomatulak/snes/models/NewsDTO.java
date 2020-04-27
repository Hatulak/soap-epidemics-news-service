package com.hatexomatulak.snes.models;

import com.project.xml.types.News;
import lombok.*;

import javax.persistence.*;
import java.text.SimpleDateFormat;
import java.util.Date;

@Data
@Entity
@NoArgsConstructor
@AllArgsConstructor
@RequiredArgsConstructor
public class NewsDTO {
    @Id
    @GeneratedValue
    private Integer newsId;
    @NonNull
    private String name;
    @NonNull
    private String desc;
    @NonNull
    private Date date;
    @NonNull
    private String imagePath;
    @ManyToOne()
    @NonNull
    @JoinColumn(name = "categoryId", nullable = false)
    private CategoryDTO category;

    public News castToNews() {
        News news = new News();
        news.setId(newsId);
        news.setName(name);
        news.setDesc(desc);
        SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy");
        String formatedDate = formatter.format(date);
        news.setDate(formatedDate);
        news.setCategoryId(category.getCategoryId());
        news.setCategoryName(category.getName());
        news.setImagePath(imagePath);
        return news;
    }
}
