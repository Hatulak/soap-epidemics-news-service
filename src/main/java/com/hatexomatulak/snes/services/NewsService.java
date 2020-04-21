package com.hatexomatulak.snes.services;

import com.hatexomatulak.snes.models.CategoryDTO;
import com.hatexomatulak.snes.models.NewsDTO;
import com.hatexomatulak.snes.repositories.CategoryRepository;
import com.hatexomatulak.snes.repositories.NewsRepository;
import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Slf4j
@RequiredArgsConstructor(onConstructor = @__(@Autowired))
@Service
public class NewsService {
    @NonNull
    private NewsRepository newsRepository;
    @NonNull
    CategoryRepository categoryRepository;

    public List<NewsDTO> findAll() {
        return newsRepository.findAll();
    }

    public Optional<NewsDTO> findById(Long id) {
        return newsRepository.findById(id);
    }


    public NewsDTO save(NewsDTO experiment) {
        return newsRepository.save(experiment);
    }

    public NewsDTO update(NewsDTO experiment) {
        return newsRepository.save(experiment);
    }


    public void delete(NewsDTO experiment) {
        @NonNull CategoryDTO category = experiment.getCategory();
        category.getNewsList().remove(experiment);
        categoryRepository.save(category);
        newsRepository.delete(experiment);
    }
}
