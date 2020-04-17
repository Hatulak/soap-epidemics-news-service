package com.hatexomatulak.snes.services;

import com.hatexomatulak.snes.models.NewsDTO;
import com.hatexomatulak.snes.repositories.NewsRepository;
import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import lombok.SneakyThrows;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

@Slf4j
@RequiredArgsConstructor(onConstructor = @__(@Autowired))
@Service
public class NewsService {
    @NonNull
    private NewsRepository newsRepository;

    public List<NewsDTO> findAll() {
        return newsRepository.findAll();
    }


    @SneakyThrows
    public Optional<NewsDTO> findById(Long id) {
        newsRepository.save(new NewsDTO("test name", "test desc ", new SimpleDateFormat("yyyy-MM-dd").parse(LocalDate.now().toString())));
        return newsRepository.findById(id);
    }


    public NewsDTO save(NewsDTO experiment) {
        return newsRepository.save(experiment);
    }

    public NewsDTO update(NewsDTO experiment) {
        return newsRepository.save(experiment);
    }

    public void delete(NewsDTO experiment) {
        newsRepository.delete(experiment);
    }
}
