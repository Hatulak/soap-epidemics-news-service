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
import org.springframework.scheduling.annotation.Async;
import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;

import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
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


    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "GetNewsIdRequest")
    @ResponsePayload
    public GetNewsResponse getNewsById(@RequestPayload GetNewsIdRequest request) throws DBException {
        NewsDTO newsDTO = null;
        try {
            newsDTO = newsService.findById(Integer.parseInt(request.getNewsid())).orElseThrow(DBException::new);
            GetNewsResponse response = new GetNewsResponse();

            response.setNews(newsDTO.castToNews());
            return response;
        } catch (DBException e) {
            log.error("[getNewsById] Problem with database, cannot find news by news. Id:  " + request.getNewsid());
            throw new DBException("Problem with database, cannot find news by news");
        }
    }

    @SneakyThrows(ParseException.class)
    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "GetNewsByDateRequest")
    @ResponsePayload
    public GetAllNewsResponse getNewsByDate(@RequestPayload GetNewsByDateRequest request) {
        NewsDTO newsDTO = null;
        SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy");
        Date parse = formatter.parse(request.getDate());
        List<NewsDTO> newsByDate = newsService.findByDate(parse);
        GetAllNewsResponse response = new GetAllNewsResponse();
        List<News> result = new ArrayList<>();
        newsByDate.forEach(p -> result.add(p.castToNews()));
        response.getNews().addAll(result);
        return response;
    }

    @SneakyThrows(ParseException.class)
    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "GetNewsByDateAndCategoryRequest")
    @ResponsePayload
    public GetAllNewsResponse getNewsByDateAndCategory(@RequestPayload GetNewsByDateAndCategoryRequest request) throws DBException {
        try {
            NewsDTO newsDTO = null;
            SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy");
            Date parse = formatter.parse(request.getDate());
            CategoryDTO categoryDTO = categoryService.findById(request.getCategoryId()).orElseThrow(DBException::new);
            List<NewsDTO> newsByDate = newsService.findByDateAndCategory(parse, categoryDTO);
            GetAllNewsResponse response = new GetAllNewsResponse();
            List<News> result = new ArrayList<>();
            newsByDate.forEach(p -> result.add(p.castToNews()));
            response.getNews().addAll(result);
            return response;
        } catch (DBException e) {
            log.error("[getNewsByDateAndCategory] Problem with database, cannot find categroy by category id :" + request.getCategoryId());
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
            SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy");
            NewsDTO newsDTO = new NewsDTO(request.getName(), request.getDesc(), formatter.parse(request.getDate()), "", categoryDTO);
            NewsDTO saved = newsService.save(newsDTO);
            CreateNewsResponse response = new CreateNewsResponse();
            response.setNews(saved.castToNews());
            return response;
        } catch (DBException e) {
            log.error("[createNews] Problem with database, cannot find category  by categoryId. Id:  " + request.getCategoryId());
            throw new DBException("Problem with database, cannot find category by categoryId");
        }

    }

    @SneakyThrows({ParseException.class, DBException.class})
    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "UpdateNewsRequest")
    @ResponsePayload
    public CreateNewsResponse updateNews(@RequestPayload UpdateNewsRequest request) {
        try {
            CategoryDTO categoryDTO = categoryService.findById(request.getCategoryId()).orElseThrow(DBException::new);
            SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy");
            NewsDTO newsDTO = newsService.findById(request.getId()).orElseThrow(DBException::new);
            newsDTO.setName(request.getName());
            newsDTO.setDesc(request.getDesc());
            newsDTO.setCategory(categoryDTO);
            newsDTO.setDate(formatter.parse(request.getDate()));
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

    @Async
    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "StoreFileRequest")
    @ResponsePayload
    public void store(@RequestPayload StoreFileRequest requestElement) throws IOException, DBException {
        try {
            NewsDTO newsDTO = newsService.findById(requestElement.getNewsid()).orElseThrow(DBException::new);
            String folderName = newsDTO.getNewsId() + "_" + newsDTO.getName();
            String filePath = fileRepository.storeFile(requestElement.getName(), requestElement.getFileData(), folderName);
            newsDTO.setImagePath(filePath);
            newsService.save(newsDTO);
        } catch (IOException e) {
            log.error("[store] Problem with saving file ", e);
            throw e;
        } catch (DBException e) {
            log.error("[deleteNews] Problem with database, cannot find news by news. Id:  " + requestElement.getNewsid());
            throw new DBException("Problem with database, cannot find news by news");
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
