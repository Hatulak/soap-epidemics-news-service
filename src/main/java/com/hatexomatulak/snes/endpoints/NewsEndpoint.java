package com.hatexomatulak.snes.endpoints;

import com.hatexomatulak.snes.exception.DBException;
import com.hatexomatulak.snes.models.CategoryDTO;
import com.hatexomatulak.snes.models.NewsDTO;
import com.hatexomatulak.snes.repositories.FileRepository;
import com.hatexomatulak.snes.services.CategoryService;
import com.hatexomatulak.snes.services.NewsService;
import com.project.xml.news.*;
import com.project.xml.types.File;
import com.project.xml.types.News;
import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import lombok.SneakyThrows;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;

import javax.xml.bind.JAXBElement;
import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;

@Slf4j
@RequiredArgsConstructor(onConstructor = @__(@Autowired))
@Endpoint
public class NewsEndpoint {
    private static final String NAMESPACE_URI = "http://www.project.com/xml/news";

    @NonNull
    private NewsService newsService;
    @NonNull
    private CategoryService categoryService;

    private FileRepository fileRepository = new FileRepository();


    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "GetNewsByIdRequest")
    @ResponsePayload
    public GetNewsResponse getNewsById(@RequestPayload GetNewsByIdRequest request) throws DBException {

        NewsDTO newsDTO = null;
        try {
            newsDTO = newsService.findById(request.getId()).orElseThrow(DBException::new);
            GetNewsResponse response = new GetNewsResponse();

            response.setNews(newsDTO.castToNews());
            return response;
        } catch (DBException e) {
            log.error("[getNewsById] Problem with database, cannot find news by news. Id:  " + request.getId());
            throw new DBException("Problem with database, cannot find news by news");
        }
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "GetAllNewsRequest")
    @ResponsePayload
    public GetAllNewsResponse getAllNews() {
        List<NewsDTO> newsDTO;
        newsDTO = newsService.findAll();
        GetAllNewsResponse response = new GetAllNewsResponse();
        List<News> result = new ArrayList<>();
        newsDTO.forEach(p -> result.add(p.castToNews()));
        response.getNews().addAll(result);
        return response;
    }

    @SneakyThrows({ParseException.class, DBException.class})
    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "CreateNewsRequest")
    @ResponsePayload
    public CreateNewsResponse createNews(@RequestPayload CreateNewsRequest request) {
        try {
            CategoryDTO categoryDTO = categoryService.findById(request.getCategoryId()).orElseThrow(DBException::new);
            SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
            NewsDTO newsDTO = new NewsDTO(request.getName(), request.getDesc(), formatter.parse(request.getDate()), categoryDTO);
            NewsDTO saved = newsService.save(newsDTO);
            CreateNewsResponse response = new CreateNewsResponse();
            response.setNews(saved.castToNews());
            return response;
        } catch (DBException e) {
            log.error("[createNews] Problem with database, cannot find category  by categoryId. Id:  " + request.getCategoryId());
            throw new DBException("Problem with database, cannot find category by categoryId");
        }

    }


    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "DeleteNewsByIdRequest")
    @ResponsePayload
    public DeleteNewsResponse deleteNews(@RequestPayload DeleteNewsByIdRequest request) throws DBException {
        //fixme after deleting object is stil bounded to category -> field: newsList
        NewsDTO newsDTO = null;
        try {
            newsDTO = newsService.findById(request.getId()).orElseThrow(DBException::new);
            newsService.delete(newsDTO);
            DeleteNewsResponse response = new DeleteNewsResponse();
            response.setResult("Success");
            return response;
        } catch (DBException e) {
            log.error("[deleteNews] Problem with database, cannot find news by news. Id:  " + request.getId());
            throw new DBException("Problem with database, cannot find news by news");
        }
    }


    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "StoreFileRequest")
    @ResponsePayload
    public void store(@RequestPayload JAXBElement<File> requestElement) throws IOException {
        File request = requestElement.getValue();
        try {
            fileRepository.storeFile(request.getName(), request);
        } catch (IOException e) {
            log.error("[store] Problem with saving file ");
            throw e;
        }
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "LoadFileRequest")
    @ResponsePayload
    public LoadFileResponse load(@RequestPayload LoadFileRequest request) throws IOException {
        String path = request.getPath();
        File file = null;
        try {
            file = fileRepository.readFile(path);
            LoadFileResponse response = new LoadFileResponse();
            response.setFile(file);
            return response;
        } catch (IOException e) {
            log.error("[load] Problem with loading file " + path);
            throw e;
        }
    }


}
