package com.hatexomatulak.snes.models;

import com.project.xml.category.Category;
import com.project.xml.types.News;
import lombok.*;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Data
@AllArgsConstructor
@NoArgsConstructor
@RequiredArgsConstructor
@Entity
public class CategoryDTO {
    @Id
    @GeneratedValue
    private Long categoryId;
    @NonNull
    private String name;
    @NonNull
    @OneToMany(mappedBy = "category", fetch = FetchType.EAGER, cascade = CascadeType.ALL)
    private List<NewsDTO> newsList;

    public Category castToCategory() {
        Category category = new Category();
        category.setId(categoryId);
        category.setName(name);
        List<News> result = new ArrayList<>();
        newsList.forEach(p -> result.add(p.castToNews()));
        category.getNews().addAll(result);
        return category;
    }
}
