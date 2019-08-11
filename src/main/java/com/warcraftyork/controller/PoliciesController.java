package com.warcraftyork.controller;

//import com.warcraftyork.bean.DBInfo;
//import com.warcraftyork.mapper.PoliciesMapper;
//import com.warcraftyork.protectu.DbUtils;
import com.warcraftyork.service.PoliciesService;
//import org.apache.ibatis.session.SqlSession;
//import org.apache.ibatis.session.SqlSessionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpSession;

@Controller
public class PoliciesController {
    @Autowired
    private PoliciesService policiesService;

    @RequestMapping("/test")
    public String test(){
        return "index";
    }

    @RequestMapping(value = "/sayHello")
    @ResponseBody
    public String sayHello(String name){
        String result;
        result = policiesService.sayHello(name);
        return result;
    }

    @GetMapping("/login")
    public String login(){
        return "login";
    }

    @RequestMapping("/policies")
    public String policies() {
        return "policies";
    }

    @RequestMapping("/logout")
    public String logout(HttpSession session){
//        session.removeAttribute(WebSecurityConfig.SESSION_KEY);
        return "redirect:/login";
    }
}
